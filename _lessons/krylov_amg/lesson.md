---
layout: page-fullwidth
title: "Krylov Solvers and Preconditioning with MueLu/Trilinos"
subheadline: "Introduction to Krylov Solvers and Preconditioning, with emphasis on Multigrid"
permalink: "lessons/krylov_amg/"
use_math: true
lesson: true
answers_google_form: "https://docs.google.com/forms/d/e/1FAIpQLSf0-OXq5gsvPG0jsli75iGbBTQx100xvTddCKGAz3sdRouUAA/viewform?usp=sf_link"
header:
 image_fullwidth: "summit_and_sierra-fs8.png"
---

## At a Glance

|Questions|Objectives|Key Points|
|How do we choose a suitable Krylov solver?|Know when to use CG or GMRES.|CG works for spd matrix and preconditioner. GMRES works for unsymmetric systems, but requires more memory.|
|How do we choose a preconditioner?|Know common sparse preconditioners.|As the size of the linear system grows, most iterative methods will require increasing number of iterations.|
|How can we improve efficiency of the solver?|Understand the basic components of multigrid.|For certain common problem classes, multigrid methods require a constant number of iterations and constant work per unknown.|

#### To begin this lesson

* [Open the Answers Form]({{page.answers_google_form}})
* Go to the directory for the krylov application
```
cd {{site.handson_root}}/krylov_amg
```

## The Problem Being Solved

The Poisson equation arises in electrostatics, incompressible fluid flow simulations, and numerous
other applications.  We will consider the Poisson equation

$$-\Delta u = f$$

on a square mesh of size $$n_x \times n_y$$ with Dirichlet boundary conditions $$u = 0$$.

It is discretized using central finite differences, leading to a symmetric positive (spd) matrix.

## The Example Source Code

For this lesson, we will be using the executable `MueLu_Stratimikos.exe` from the MueLu package of Trilinos which allows us to test a variety of solvers and preconditioners.

For the first part of the lesson, we will be running on a single MPI rank, so no need to ask for a massive allocation.

The executable takes several command line arguments that influence the linear system that is generated on the fly or read in from file.
A complete set of options will be printed by typing
```
./MueLu_Stratimikos.exe --help
```
The most important ones are:
```
Usage: ./MueLu_Stratimikos.exe [options]
  options:
  --help                               Prints this help message
  --nx                   int           mesh points in x-direction.
                                       (default: --nx=100)
  --ny                   int           mesh points in y-direction.
                                       (default: --ny=100)
  --nz                   int           mesh points in z-direction.
                                       (default: --nz=100)
  --matrixType           string        matrix type: Laplace1D, Laplace2D, Laplace3D, ...
                                       (default: --matrixType="Laplace2D")
  --xml                  string        read parameters from an xml file
                                       (default: --xml="stratimikos_ParameterList.xml")
  --yaml                 string        read parameters from a yaml file
                                       (default: --yaml="")
  --matrix               string        matrix data file
                                       (default: --matrix="")
  --rhs                  string        rhs data file
                                       (default: --rhs="")
  --coords               string        coordinates data file
                                       (default: --coords="")
  --nullspace            string        nullspace data file
                                       (default: --nullspace="")
```

Solvers (such as CG and GMRES) and preconditioners (such as Jacobi, Gauss-Seidel and multigrid) are configured via parameter files.

Trilinos supports both XML and YAML files.
In what follows, we will be modifying modifying `stratimikos_ParameterList.xml` to explore a variety of solvers and preconditioners.

By default, the XML file `stratimikos_ParameterList.xml` is read.
If you want to keep track of your changes and work with different input files, this default can be overridden with `--xml=another-file.xml`.


## Running the Example

### Set 1 - Krylov solver, no preconditioner

The default Krylov method is GMRES, and no preconditioner is used.

<img src="arrow.png" width="30"> Run
```
./MueLu_Stratimikos.exe
```

#### Expected Behavior/Output

You should see output like this:

```
========================================================
Xpetra::Parameters
 Linear algebra library: Tpetra
Galeri::Xpetra::Parameters<int>
 Matrix type: Laplace2D
 Problem size: 10000 (100x100)
Processor subdomains in x direction: 1
Processor subdomains in y direction: 1
Processor subdomains in z direction: -1
========================================================
Galeri complete.
========================================================

  *******************************************************
  ***** Belos Iterative Solver:  Pseudo Block Gmres
  ***** Maximum Iterations: 100
  ***** Block Size: 1
  ***** Residual Test:
  *****   Test 1 : Belos::StatusTestImpResNorm<>: (2-Norm Res Vec) / (2-Norm Prec Res0), tol = 1e-08
  *******************************************************
  Iter   0, [ 1] :    1.000000e+00
  Iter  10, [ 1] :    2.934358e-03
  Iter  20, [ 1] :    4.605673e-04
  Iter  30, [ 1] :    1.647752e-04
  Iter  40, [ 1] :    7.453272e-05
  Iter  50, [ 1] :    4.822835e-05
  Iter  60, [ 1] :    2.768790e-05
  Iter  70, [ 1] :    1.712668e-05
  Iter  80, [ 1] :    1.194621e-05
  Iter  90, [ 1] :    9.782121e-06
  Iter 100, [ 1] :    7.221948e-06
  Passed.......OR Combination ->
    Failed.......Number of Iterations = 100 == 100
    Unconverged..(2-Norm Res Vec) / (2-Norm Prec Res0)
                 residual [ 0 ] = 7.22195e-06 > 1e-08
```

#### Examining Results

We observe the following:
- We constructed a 2D Laplace problem on a square mesh of 100 x 100 nodes, resulting in a linear system of 10000 unknowns.
- We have set two termination criteria for the solve: 100 iterations or a reduction of the residual norm by 8 orders of magnitude.
- The solve failed, since we reached 100 iterations, but only reduced the residual norm by a factor of 7e-06.

Now, modify the input file to use the conjugate gradient method.

<img src="arrow.png" width="30"> Change the `Solver Type` parameter on line 17 of `stratimikos_ParameterList.xml` to `Pseudo Block CG` and rerun.

{% include qanda question='Do you see any significant changes in convergence behavior?' answer='No, neither solver manages to converge in less than 100 iterations.' %}

{% include qanda question='Why is it preferable to use conjugate gradients over GMRES in this case?' answer='CG has significantly lower memory requirements, since it uses a short recurrence. GMRES, on the other hand, has to keep the entire Krylov space around.' %}

You can check the last answer by comparing the approximate memory usage of CG and GMRES using
```
/usr/bin/time -v ./MueLu_Stratimikos.exe --nx=1000 --ny=1000 2>&1 | grep "Maximum resident set size"
```
We used a larger problem to be able to see the difference more clearly.

In what follows, we will be using the CG solver.

<!-- IS THERE A BETTER WAY OF CHECKING PEAK MEMORY? -->

---

### Set 2 - Krylov solver, simple preconditioners

We now explore some simple (and quite generic) options for preconditioning the problem.

By default, the `Preconditioner Type` parameter was set to `None` on line 59, meaning no preconditioning.
Use `Ifpack2` instead.
Ifpack2 is another Trilinos package which provides a number of different simple preconditioners.

Moreover, have a look at the configuration for Ifpack2, starting on line 74.
```xml
<ParameterList name="Ifpack2">
  <Parameter name="Prec Type" type="string" value="relaxation"/>
  <ParameterList name="Ifpack2 Settings">
    <Parameter name="relaxation: type" type="string" value="Gauss-Seidel"/>
    <Parameter name="relaxation: sweeps" type="int" value="1"/>
  </ParameterList>
</ParameterList>
```
This means that a single sweep of Gauss-Seidel is used.

<img src="arrow.png" width="30"> Rerun the code.

{% include qanda question='Why did the solve become even worse?' answer='Gauss-Seidel is an unsymmetric preconditioner, but CG needs a symmetric one!' %}

Switch the `relaxation: type` from `Gauss-Seidel` to `Symmetric Gauss-Seidel`.
This corresponds to one forward and one backward sweep of Gauss-Seidel.

<img src="arrow.png" width="30"> Rerun to verify that the solver is now converging.

We can strengthen the preconditioner by increasing the number of symmetric Gauss-Seidel sweeps we are using as a preconditioner.

<img src="arrow.png" width="30"> Switch `relaxation: sweeps` to 3, rerun and verify that the number of iterations further decreased.

Now, we will check whether we have created a scalable solver strategy.

<img src="arrow.png" width="30"> Record the number of iterations for different problem sizes by running
```
./MueLu_Stratimikos.exe --nx=50 --ny=50
./MueLu_Stratimikos.exe --nx=100 --ny=100
./MueLu_Stratimikos.exe --nx=200 --ny=200
```
(This means that we are running the same 2D Laplace problem as above, but on meshes of size 50x50, etc.)

{% include qanda question='Is the solver scalable?' answer='No, the number of iterations increases with the problem size.' %}

The number of iterations taken by CG scales with the square root of the condition number $$\kappa(PA)$$ of the preconditioned system, where $$P$$ is the preconditioner.

{% include qanda question='Based on the iterations you recorded, how does this condition number roughly scale with respect to the number of unknowns?' answer='In each step, the number of iterations grows by a factor of 2, and the number of unknows grows by a factor of 4. Hence the condition number is proportional to the number of unknowns.' %}

---

### Set 3 - Krylov solver, multigrid preconditioner

The reason that the Gauss-Seidel preconditioner did not work well is that it effectively only reduces error locally, but not globally.
We hence need a global mechanism of error correction, which can be provided by adding one or more coarser grids.

<img src="arrow.png" width="30"> On line 59 switch the `Preconditioner Type` to `MueLu`, which is an algebraic multigrid package in Trilinos, and run
```
./MueLu_Stratimikos.exe --nx=50 --ny=50
./MueLu_Stratimikos.exe --nx=100 --ny=100
./MueLu_Stratimikos.exe --nx=200 --ny=200
```

{% include qanda question='Is the solver scalable?' answer='Yes, the number of iterations stays more or less constant as we increase the problem size.' %}

<!-- The cost of a single mat-vec scales with the number of unknowns because the number of entries per row is bounded and small. -->
<!-- Since the number of iterations is constant, we (experimentally) have verified that multigrid has optimal complexity. -->
<!-- This means that any changes that we will make from here on can only lead to a constant factor improvement. -->

#### Understanding information about the multigrid preconditioner

Let''s look a little more closely at the output from the largest example.

<img src="arrow.png" width="30"> Rerun:
```
./MueLu_Stratimikos.exe --nx=200 --ny=200
```
The multigrid summary provides the following information:

* The number of multigrid levels created, including the linear system of interest
* Operator complexity
* Smoother complexity
* The multigrid cycle type
* Matrix statistics for each level (rows, number of nonzeros, number of processors)
* The smoother used on each level

The operator complexity is given by the formula

$$\frac{\Sigma_0^L nnz(A_i)}{nnz(A_0)},$$

where $$A_0$$ is the fine level matrix.

{% include qanda question='How does the operator complexity help the user assess potential performance?' answer='
The complexity gives the ratio of nonzeros in all matrices compared to the fine level matrix.  This is roughly the ratio of FLOPs required by
a matrix-vector product performed on each matrix relative to the fine level matrix.' %}

The smoother complexity is the ratio of FLOPS required by smoothers on all levels to FLOPs required by just the fine level smoother.

{% include qanda question='Why might the operator complexity and smoother complexity differ?'
answer='A smoother such as an incomplete factorization will have a much higher FLOP intensity than a matrix-vector product.' %}

#### Effect of different smoothers

The first adjustment that we want to make is to select different smoothers.
This involves the following trade-off: choosing a more effective smoother should reduce the number of iterations, but might involve more computation.

By default, we use a single sweep of Jacobi smoothing, which is very cheap.

<img src="arrow.png" width="30"> First, we run
```
./MueLu_Stratimikos.exe --timings --nx=1000 --ny=1000
```
to display timing information on a large enough problem.
The relevant timer to look at is `Belos: PseudoBlockCGSolMgr total solve time`.
(You might want to run this more than once in case you are experiencing some system noise.)
Since there are quite a lot of timers, you could grep for the iteration count and the timer by appending
```|  egrep "total solve time|Number of Iterations"``` to the command, i.e.,
```
./MueLu_Stratimikos.exe --timings --nx=1000 --ny=1000 |  egrep "total solve time|Number of Iterations"
```

We know that Gauss-Seidel is a better smoother than Jacobi.
There are two ways of using Gauss-Seidel while keeping the preconditioner symmetric:
you can either use different directions in the sweeps in pre- and post-smoothing, or use a symmetric Gauss-Seidel smoother for both.

<img src="arrow.png" width="30"> Make the required changes in the input file (starting from line 118) and compare the timings with the Jacobi case.

{% include qanda question='Do you see an improvement?' answer='Yes. For symmetric Gauss-Seidel, the number of iterations decreases.  For forward Gauss-Seidel
for pre-smoothing and backwards Gauss-Seidel for post-smoothing, both number of iterations and time-to-solution are reduced.' %}

{% include qanda question='Try increasing the number of MPI ranks to 2, 4, and 8, respectively.  What happens?' answer='The number of iterations grows
slightly.  The solution time decreases.' %}

{% include qanda question='Do you think that Gauss-Seidel is well suited for use on massively parallel architectures such as GPUs?' answer='Gauss-Seidel has
limited opportunities for parallelism.  Equation $$i$$ cannot be solved until all equations $$j, j<i$$ that $$i$$ depends on have been solved.' %}
Hint: Have a look at the [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#Algorithm).

Another common smoother is a matrix polynomial, specifically, a Chebyshev polynomial.  This type smoother has certain advantages over relaxation methods
like Jacobi or Gauss-Seidel.
  - Chebyshev will have better convergence properties than Jacobi.
  - The Chebyshev computational kernel is a sparse matrix-vector multiply (SpMV), which is invariant with respect to the number of processes.
  - The SpMV kernel is naturally parallelizable with many high-performance implementations.  There are limited opportunities for parallelism in Gauss-Seidel,
    e.g., coloring.

<img src="arrow.png" width="30"> Change the input file to use Chebyshev smoothing instead of Gauss-Seidel, and repeat the experiment.
```
mpirun -np 1 ./MueLu_Stratimikos.exe --timings --matrixType=Laplace3D --nx=20 --ny=20 --nz=20
mpirun -np 10 ./MueLu_Stratimikos.exe --timings --matrixType=Laplace3D --nx=20 --ny=20 --nz=20
```

{% include qanda question='What do you observe?' answer='The Gauss-Seidel smoother convergence degrades slightly as the number of MPI ranks is increased.  The Chebyshev smoother convergence is unaffected by the number of ranks.' %}

{% include qanda question='Can you explain your observations?' answer='First, when Gauss-Seidel is run with
more than one MPI rank,
the order in which unknowns are updated is different than in serial.
Second, the Ifpack2 Gauss-Seidel implementation is additive. Each MPI rank simultaneously runs
Gauss-Seidel on the process-local unknowns, and communication occurs only after all MPI ranks have completed their
local solves.
In a true multiplicative implementation, each MPI rank would solve its local unknowns in turn, with communication between
each rank solve.  Third, Chebyshev is relatively unaffected by the number of MPI processes due its use of the SpMV kernel.' %}

Choosing a smoother that is computationally inexpensive but with poor convergence properties can result in a large number of solver iterations.
Choosing a smoother that is computationally expensive but with good convergence properties can result in a small number of solver iterations, but overall long
run times.

#### Changing the behavior of the grid transfer operators

##### Change coarsening procedure by setting the aggregation threshold parameter

In practice, you will likely encounter matrices arising from partial differential equation with material coefficient variation, mesh stretching,
or some other directional variability.  In these cases, it's often beneficial to ignore weak connections between unknowns.
<!--
JHU: This won''t render properly
A technical
definition of a weak matrix connection $$a_{ij}$$ is $$\|a_{ij}\| < \epsilon \sqrt{(\|a_{ii} a_{jj}\|}$$, where $$\epsilon \geq 0$$ is a user-specified value.
-->

<img src="arrow.png" width="30"> Run the following example.

```
./MueLu_Stratimikos.exe --nx=50 --ny=50
```

This example solves a Poisson equation discretized on a regular $$50\times 50$$ mesh with square elements.

[<img src="isotropic-mesh.png" width="400">](isotropic-mesh.png)

<img src="arrow.png" width="30"> Now run the following example.

```
./MueLu_Stratimikos.exe --nx=50 --ny=50 --stretchx=10
```

This example solves a Poisson equation discretized on a regular $$50\times 50$$ mesh, but now each element has an
_aspect ratio_ of 10 to 1.

[<img src="stretched-mesh.png" width="400">](stretched-mesh.png)

The corresponding PDE is

$$\epsilon u_{xx} + u_{yy} = f, \epsilon=0.1$$.

The matrix stencil looks like
[<img src="anisotropic-stencil.png" width="400">](anisotropic-stencil.png)

{% include qanda question='What do you observe in the previous runs?' answer='The first problem, which has an isotropic underlying mesh, converges in 7 iterations.  The second
problem converges in 22 iterations.'%}

A smoother like Gauss-Seidel works by averaging the values of neighboring unknowns:

$$x_i = \frac{1}{a_{ii}} (b_i - \Sigma_{j\neq i} a_{ij} x_j).$$

In the second anisotropic case, the smoothing is primarily
influenced by its vertical neighbors.  These connections are called "strong" connections.

This same idea of strong connections can help guide creation of the next coarse level.   Unknowns that are strongly connected are grouped together into
_aggregates_.  The option to control this in MueLu is `aggregation: drop tol`.

<img src="arrow.png" width="30"> Now rerun the second anisotropic example, but modifying the parameter `aggregation: drop tol` on line 110 in the input deck to have a value of $$0.02$$.

{% include qanda question='What effect does modifying the threshold value have on the multigrid convergence?' answer='For the anisotropic problem, the multigrid
solver converges in 7 iterations.'%}

We plot the resulting aggregates.  (Recall that aggregates are groups of fine DOFs that form coarse DOFs.)

[<img src="muelu-drop.png" width="400">](muelu-drop.png)

(If you want to reproduce this, have a look at the parameter `aggregation: export visualization data`.)

We can see that the aggregates are now entirely aligned with the $$y$$-direction.

---

There are many other options that one can use to affect the AMG behavior.  Some of these can be found below in the Evening Activity section.

---


## Out-Brief

In this lesson, we have developed a scalable solver for a simple test problem, the Poisson equation.

A good choice of solver and preconditioner will depend significantly on the problem that needs to be solved, and are often the topic of active research.

- CG works for symmetric, GMRES for unsymmetric systems, but GMRES has a larger memory footprint.
  (Trilinos has many more specialized Krylov solvers.
  The [Belos Doxygen](https://trilinos.org/docs/dev/packages/belos/doc/html/index.html) is a good starting point, but some newer communication reducing
  algorithms have not yet been fully documented.)

- One-level preconditioners (such as Jacobi and Gauss-Seidel) will often not lead to a scalable solver.

- Multigrid solvers are scalable (on Poisson), but getting good performance often involves some parameter tuning.

---

### Further Reading

[Trilinos GitHub Repo](https://github.com/trilinos/Trilinos)
Please feel free to submit questions, feature requests and bug reports to the issue tracker.

[MueLu webpage](https://trilinos.github.io/muelu.html)

[MueLu Doxygen](https://trilinos.org/docs/dev/packages/muelu/doc/html/index.html)

[MueLu User Guide](https://trilinos.github.io/pdfs/mueluguide.pdf)

[Longer, in-depth MueLu tutorial](https://trilinos.github.io/muelu_tutorial.html)

---

### Evening Activity 1

You can compare the scaling results from Set 2 to the case when no preconditioner is used.
You should increase the `Maximum Iterations` parameter of the CG solve to at least 500 for this, so that the solver actually converges.

What you should observe is that the preconditioner significantly cuts down on the number of iterations, but that the scaling of the solver remains the same.

---

### Evening Activity 2 - Krylov solver, parallel multigrid preconditioner and performance optimizations

Running the same problem in parallel using MPI is as simple as running
```
mpiexec -n 12 ./MueLu_Stratimikos.exe
```
(Each node of Cooley has 2 sockets of 6 cores each, so you still only need a single node for this to work.)

In the output, you should find a summary of the multigrid hierarchy:
```
--------------------------------------------------------------------------------
---                            Multigrid Summary                             ---
--------------------------------------------------------------------------------
Number of levels    = 3
Operator complexity = 1.41
Smoother complexity = 1.59
Cycle type          = V

level  rows   nnz    nnz/row  c ratio  procs
  0  10000  49600  4.96                  12
  1  1792   17428  9.73     5.58         12
  2  220    3110   14.14    8.15         12

```
We see that our multigrid has 3 levels, the coarsest of which has only 220 unknowns.
However, this small matrix lives on all 12 ranks, which means that a multiplication which it involves very little computation per MPI rank, but a lot of communication.
It would be better for smaller matrices to live on smaller sub-communicators.

#### Repartitioning

Enable the repartitioning option of MueLu by uncommenting the relevant block in the input file. (That's all the options starting with `repartitioning: `.)

What this means is that based on several criteria, MueLu will try to repartition coarser level matrices onto a sub-communicator of smaller size, thereby improving the volume-to-surface ratio.
By default, MueLu uses a partitioner from Zoltan2, a Trilinos package that provides several algorithms for partitioning, load-balancing, ordering and coloring.

Rerun the code to verify that the coarsest level now only lives on a single MPI rank.


#### Other types of multigrid hierarchies

By default, MueLu builds a so-called `smoothed aggregation` multigrid preconditioner.
What this means is that in order to build coarser matrices, connected unknowns are grouped into aggregates.
A tentative prolongation operator is formed, which preserves a pre-defined near-nullspace.
(In the case of our Poisson equation, that's the constant function.)
In order to obtain provable scalability, this operator is smoothed using a single step of Jacobi to obtain the final prolongator.
This implies, however, that the prolongator contains more non-zeros than the tentative prolongator.
Switching the parameter `multigrid algorithm` to `unsmoothed` skips the smoothing step and uses the tentative prolongator directly.

Compare timings for `sa` and `unsmoothed`.
{% include qanda question='Can you see an improvement?' answer='No, both iteration count and time-to-solution actually increase.' %}

{% include qanda question='Looking at the respective multigrid summaries, can you observe a reduction of non-zeros (nnz)?' answer='Yes, the number of nonzeros is reduced.' %}

The reason for the above observation is that the number of unknowns is not reduced significantly enough to offset the deteriorated convergence properties.
Problems which have more non-zeros per row (e.g. in higher spatial dimension) can benefit more from this change.

#### MueLu on next-generation platforms

MueLu has specialized kernels that allow it to run on next-generation computing platforms such as KNLs and GPUs, using a Kokkos backend.
If MueLu has been compiled with OpenMP or CUDA support, this code can be enabled at runtime by setting the parameter `use kokkos refactor` to true.

Add the `openmpi-2.1.5` and `cuda-9.1` modules to your environment.
Try running
```
export CUDA_LAUNCH_BLOCKING=1
export CUDA_MANAGED_FORCE_DEVICE_ALLOC=1
./MueLu_Stratimikos_gpu.exe
```
with the refactor option set.

If you want to use both GPUs, run
```
mpiexec -n 2 ./MueLu_Stratimikos_gpu.exe --kokkos-ndevices=2
```

---

### Running your own problem

The executable has the option to load the linear system and the right-hand side from MatrixMarket files, e.g.,
```
./MueLu_Stratimikos.exe --matrix=poisson-matrix.m --rhs=poisson-rhs.m --coords=poisson-coords.m
```
