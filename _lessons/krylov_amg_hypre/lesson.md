---
layout: page-fullwidth
title: "Krylov Solvers and Algebraic Multigrid"
subheadline: "Demonstrate utility of multigrid"
permalink: "lessons/krylov_amg_hypre/"
use_math: true
lesson: true
header:
 image_fullwidth: "AMG-hypre.png"
---

## At a Glance

|Why multigrid over a Krylov<br>solver for large problems?|Understand multigrid concept.|Faster convergence,<br>better scalability.|
|Why use more aggressive<br>coarsening for AMG?|Understand need for low complexities.|Lower memory use, faster times,<br>but more iterations.|
|Why a structured solver<br>for a structured problem?|Understand importance of<br>suitable data structures|Higher efficiency,<br>faster solve times.|


## The Problem Being Solved

We consider the Poisson equation

$$-\Delta u = f$$

on a cuboid of size $$n_x \times n_y \times n_z$$ with Dirichlet boundary conditions $$u = 0$$.

It is discretized using central finite differences, leading to a symmetric positive matrix.

**Note:** To begin this lesson...
* [Open the Answers Form](https://docs.google.com/forms/d/e/1FAIpQLSeZAaguErZ-VTtzQSeYfkrpkck_ki2-OZ1uIbLRXjc6NW8-gg/viewform?usp=sf_link)
```
cd {{site.handson_root}}/krylov_amg
```


## The Example Source Code

For the first part of the hands-on lessons we will use the executable ij. Various solver, problem and parameter options can be invoked by adding them to the command line.
A complete set of options will be printed by typing
```
./ij -help
```
Here is an excerpt of the output of this command with all the options relevant for the hands-on lessons.

```
Usage: ij [<options>]

Choice of Problem:
  -laplacian [<options>] : build 7pt 3D laplacian problem (default)
  -difconv [<opts>]      : build convection-diffusion problem
    -n <nx> <ny> <nz>    : problem size per process
    -P <Px> <Py> <Pz>    : process topology
    -a <ax>              : convection coefficient
  -rotate [<opts>]       : build 2D problem with rotated anisotropy
    -eps <eps>           : anisotropy for rotated problem
    -alpha <alpha>       : angle by which anisotropy is rotated

Choice of solver:
   -amg                  : AMG only
   -amgpcg               : AMG-PCG
   -pcg                  : diagonally scaled PCG
   -amggmres             : AMG-GMRES with restart k (default k=10)
   -gmres                : diagonally scaled GMRES(k) (default k=10)
   -amgbicgstab          : AMG-BiCGSTAB
   -bicgstab             : diagonally scaled BiCGSTAB
   -k  <val>             : dimension Krylov space for GMRES

.....

  -tol  <val>            : set solver convergence tolerance = val
  -max_iter  <val>       : set max iterations 
  -agg_nl  <val>         : set number of aggressive coarsening levels (default:0)
  -iout <val>            : set output flag
       0=no output    1=matrix stats
       2=cycle stats  3=matrix & cycle stats

  -print                 : print out the system
```

## Running the Example

### First Set of Runs (Krylov Solvers)

Run the first example for a small problem of size 27000 using restarted GMRES with a Krylov space of size 10.
```
./ij -n 30 30 30 -gmres
```

#### Expected Behavior/Output

You should get something that looks like this
```
Running with these driver parameters:
  solver ID    = 4

    (nx, ny, nz) = (30, 30, 30)
    (Px, Py, Pz) = (1, 1, 1)
    (cx, cy, cz) = (1.000000, 1.000000, 1.000000)

    Problem size = (30 x 30 x 30)

=============================================
Generate Matrix:
=============================================
Spatial Operator:
  wall clock time = 0.000000 seconds
  wall MFLOPS     = 0.000000
  cpu clock time  = 0.000000 seconds
  cpu MFLOPS      = 0.000000

  RHS vector has unit components
  Initial guess is 0
=============================================
IJ Vector Setup:
=============================================
RHS and Initial Guess:
  wall clock time = 0.000000 seconds
  wall MFLOPS     = 0.000000
  cpu clock time  = 0.000000 seconds
  cpu MFLOPS      = 0.000000

Solver: DS-GMRES
HYPRE_GMRESGetPrecond got good precond
=============================================
Setup phase times:
=============================================
GMRES Setup:
  wall clock time = 0.000000 seconds
  wall MFLOPS     = 0.000000
  cpu clock time  = 0.000000 seconds
  cpu MFLOPS      = 0.000000

=============================================
Solve phase times:
=============================================
GMRES Solve:
  wall clock time = 0.270000 seconds
  wall MFLOPS     = 0.000000
  cpu clock time  = 0.270000 seconds
  cpu MFLOPS      = 0.000000


GMRES Iterations = 392
Final GMRES Relative Residual Norm = 9.915663e-09
Total time = 0.270000
```

Note the total time and the number of iterations.
Now increase the Krylov subspace by changing input to -k to 40, and finally 75.

{% include qanda question='What do you observe about the number of iterations and times?' answer='Number of iterations and times generally improve except for the last run, which is somewhat slower because the last iterations are more expensive. Iterations: 392, 116, 73. Times: 0.27, 0.16, 0.17.' %}

{% include qanda question='How many restarts were required for the last run using -k 75?'  answer='None, since the number of iterations is 73. Here full GMRES was used.'%}

Now solve this problem using -pcg and -bicgstab.

{% include qanda question='What do you observe about the number of iterations and times for all three methods? Which method is the fastest and which one has the lowest number of iterations?' answer='Conjugate gradient takes 74 iterations and 0.04 seconds, BiCGSTAB 51 iterations and 0.05 seconds. Conjugate gradient has the lowest time, but BiCGSTAB has the lowest number of iterations.' %}

{% include qanda question='Why is BiCGSTAB slower than PCG?' answer='It requires two matrix vector operations and additional vector operations per iteration, and thus each iteration takes longer than an iteration of PCG.' %}

Now let us scale up the problem starting with a cube of size $$50 \times 50 \times 50$$ on one process:
```
mpiexec -n 1 ./ij -n 50 50 50 -pcg -P 1 1 1
```
Now we increase the problem size to a cube of size $$100 \times 100 \times 100$$
by increasing the number of processes to 8 using the process topology -P 2 2 2.
```
mpiexec -n 8 ./ij -n 50 50 50 -pcg -P 2 2 2
```
{% include qanda question='What happens to convergence and solve time?' answer='
the number of iterations increases from 124 to 249, the time from 0.55 seconds to 1.46 seconds.' %}



### Second Set of Runs (Algebraic Multigrid)

Now perform the previous weak scaling study using algebraic multigrid starting with
```
mpiexec -n 1 ./ij -n 50 50 50 -amg -P 1 1 1
```
followed by
```
mpiexec -n 8 ./ij -n 50 50 50 -amg -P 2 2 2
```

{% include qanda question='What happens to convergence and solve time now?' answer='AMG solves the problem using significantly less iterations, and time increases somewhat slower.  Number of iterations: 12, 23.
Total time: 0.51, 1.18 seconds.' %}

Now repeat the scaling study using AMG as a preconditioner for CG:
```
mpiexec -n 1 ./ij -n 50 50 50 -amgpcg -P 1 1 1
```
```
mpiexec -n 8 ./ij -n 50 50 50 -amgpcg -P 2 2 2
```
{% include qanda question='What happens to convergence and solve time now?' answer='Using PCG preconditioned with AMG further decreases the number of iterations and solve times.  Number of iterations: 8, 11.  Total time: 0.47, 0.89 seconds.' %}

Now let us take a look at the complexities of the last run by printing some setup statistics:
```
mpiexec -n 8 ./ij -n 50 50 50 -amgpcg -P 2 2 2 -iout 1
```
You should now see the following statistics:
```
HYPRE_ParCSRPCGGetPrecond got good precond


 Num MPI tasks = 8

 Num OpenMP threads = 1


BoomerAMG SETUP PARAMETERS:

 Max levels = 25
 Num levels = 8

 Strength Threshold = 0.250000
 Interpolation Truncation Factor = 0.000000
 Maximum Row Sum Threshold for Dependency Weakening = 1.000000

 Coarsening Type = HMIS
 measures are determined locally


 No global partition option chosen.

 Interpolation = extended+i interpolation

Operator Matrix Information:

            nonzero         entries per row        row sums
lev   rows  entries  sparse  min  max   avg       min         max
===================================================================
 0 1000000  6940000  0.000     4    7   6.9   0.000e+00   3.000e+00
 1  499594  8430438  0.000     7   42  16.9  -2.581e-15   4.000e+00
 2  113588  5267884  0.000    18   83  46.4  -9.556e-15   5.515e+00
 3   14088  1099948  0.006    16  126  78.1  -2.339e-14   8.187e+00
 4    2585   235511  0.035    11  183  91.1  -9.932e-14   1.622e+01
 5     366    25888  0.193    11  181  70.7   2.032e-01   4.293e+01
 6      44     1228  0.634    14   44  27.9   9.754e+00   1.501e+02
 7       9       77  0.951     7    9   8.6   1.198e+01   3.267e+02


Interpolation Matrix Information:
                 entries/row    min     max         row sums
lev  rows cols    min max     weight   weight     min       max
=================================================================
 0 1000000 x 499594   1   4   1.429e-01 4.545e-01 5.000e-01 1.000e+00
 1 499594 x 113588   1   4   1.330e-02 5.971e-01 2.164e-01 1.000e+00
 2 113588 x 14088   1   4  -1.414e-02 5.907e-01 5.709e-02 1.000e+00
 3 14088 x 2585    1   4  -4.890e-01 6.377e-01 2.236e-02 1.000e+00
 4  2585 x 366     1   4  -1.185e+01 5.049e+00 8.739e-03 1.000e+00
 5   366 x 44      1   4  -2.597e+00 3.480e+00 6.453e-03 1.000e+00
 6    44 x 9       1   4  -2.160e-01 8.605e-01 -6.059e-02 1.000e+00


     Complexity:    grid = 1.630274
                operator = 3.170169
                memory = 3.837342




BoomerAMG SOLVER PARAMETERS:

  Maximum number of cycles:         1
  Stopping Tolerance:               0.000000e+00
  Cycle type (1 = V, 2 = W, etc.):  1

  Relaxation Parameters:
   Visiting Grid:                     down   up  coarse
            Number of sweeps:            1    1     1
   Type 0=Jac, 3=hGS, 6=hSGS, 9=GE:     13   14     9
   Point types, partial sweeps (1=C, -1=F):
                  Pre-CG relaxation (down):   0
                   Post-CG relaxation (up):   0
                             Coarsest grid:   0

```
This output contains some statistics for the AMG preconditioner. It shows the number of levels, the average number of nonzeros in total and per row for each matrix $$A_i$$ as well as each interpolation operator $$P_i$$.
It also shows the operator complexity, which is defined as the sum of the number of nonzeroes of all operators $$A_i$$
divided by the number of nonzeroes of the original matrix $$A$$:
$$\frac{\sum_i^L {nnz(A_i)}}{nnz(A)}$$.
It also gives the memory complexity, which is defined by
$$\frac{\sum_i^L {nnz(A_i + P_i)}}{nnz(A)}$$.

{% include qanda question='What do you notice about the average number of nonzeroes per row across increasing levels?' answer='It increases significantly  through level 4 and decreases after that. It is much larger than the original level.'
 %}

{% include qanda question='What causes this growth?' answer='It is caused by the Galerkin product, i.e. the product of the three matrices R, A, and P.'
 %}
{% include qanda question='Is the operator complexity acceptable?' answer='No, we would prefer a number that is closer to 1.'  %}

Now, let us see what happens if we coarsen more aggressively on the finest level:

```
mpiexec -n 8 ./ij -n 50 50 50 -amgpcg -P 2 2 2 -iout 1 -agg_nl 1
```
We now receive the following output for average number of nonzeroes and complexities:
```
Operator Matrix Information:

            nonzero         entries per row        row sums
lev   rows  entries  sparse  min  max   avg       min         max
===================================================================
 0 1000000  6940000  0.000     4    7   6.9   0.000e+00   3.000e+00
 1   79110  1427282  0.000     6   33  18.0  -1.779e-14   8.805e+00
 2   16777   817577  0.003    12   91  48.7  -2.059e-14   1.589e+01
 3    2235   153557  0.031    19  132  68.7   6.580e-14   3.505e+01
 4     309    18445  0.193    17  160  59.7   1.255e+00   8.454e+01
 5      50     1530  0.612    13   50  30.6   1.521e+01   3.237e+02
 6       5       25  1.000     5    5   5.0   6.338e+01   3.572e+02


Interpolation Matrix Information:
                 entries/row    min     max         row sums
lev  rows cols    min max     weight   weight     min       max
=================================================================
 0 1000000 x 79110   1   9   2.646e-02 9.722e-01 2.778e-01 1.000e+00
 1 79110 x 16777   1   4   7.709e-03 1.000e+00 2.709e-01 1.000e+00
 2 16777 x 2235    1   4   2.289e-03 7.928e-01 5.909e-02 1.000e+00
 3  2235 x 309     1   4  -6.673e-02 5.759e-01 4.594e-02 1.000e+00
 4   309 x 50      1   4  -6.269e-01 3.959e-01 2.948e-02 1.000e+00
 5    50 x 5       1   4  -1.443e-01 1.083e-01 -4.496e-02 1.000e+00


     Complexity:    grid = 1.098486
                operator = 1.348475
                memory = 1.700654
```
As you can see, the number of levels, the number of nonzeroes per rows and the complexities have decreased.
{% include qanda question='How does the number of iterations and the time change?' answer='The number of iterations increases (17 vs. 11), but total time is less (0.69 vs 0.89)'  %}

Now let us use aggressive coarsening in the first two levels.
```
mpiexec -n 8 ./ij -n 50 50 50 -amgpcg -P 2 2 2 -iout 1 -agg_nl 2
```
{% include qanda question='What happens to complexities, number of iterations and total time?' answer='Complexities decrease further to 1.22, but the number of iterations is increasing to 26 and total time increases as well. Choosing to aggressively coarsen on the second level does not lead to further time savings, but gives further memory savings. If achieving the shortest time is the objective, coarsen aggressively on the second level is not adviced.'  %}

So far, we achieved the best overall time to solve a Poisson problem on a cube of size $$100 \times 100 \times$$ using conjugate gradient preconditioned with AMG with one level of aggressive coarsening.

How would a structured solver perform on this problem?
We now use the driver for the structured interface, which will also give various input options by typing
```
./struct -help
```

To run the structured solver PFMG for this problem type
```
mpiexec -n 8 ./struct -n 50 50 50 -P 2 2 2 -pfmg
```
{% include qanda question='How does the number of iterations and the time change?' answer='The number of iterations 35, but the total time is less (0.36)'  %}

Now run it as a preconditioner for conjugate gradient.
```
mpiexec -n 8 ./struct -n 50 50 50 -pfmgpcg -P 2 2 2
```
{% include qanda question='How does the number of iterations and the time change?' answer='The number of iterations 14, but the total time is less (0.24)'  %}

To get even better total time, now run the non-Galerkin version.

```
mpiexec -n 8 ./struct -n 50 50 50 -pfmgpcg -P 2 2 2 -rap 1
```
{% include qanda question='How does the number of iterations and the time change?' answer='The number of iterations remains 14, but the total time is less (0.21)'  %}


### Evening exercises

We now consider the diffusion-convection equation

$$-\Delta u + a \nabla \cdot u = f$$

on a cuboid with Dirichlet boundary conditions.

The diffusion part is discretized using central finite differences, and upwind finite differences are used for the advection term.
For $$a = 0$$ we just get the Poisson equation, but when $$a > 0$$ we get a nonsymmetric linear system.

Now let us apply Krylov solvers to the convection-diffusion equation with $$a=10$$, starting with conjugate gradient.

```
./ij -n 50 50 50 -difconv -a 10 -pcg
```
{% include qanda question='What do you observe? Why?' answer='PCG fails, because the linear system is nonsymmetric.' %}

Now try GMRES(20), BiCGSTAB, and AMG with and without aggressive coarsening.
```
./ij -n 50 50 50 -difconv -a 10 -gmres -k 20
```
```
./ij -n 50 50 50 -difconv -a 10 -bicgstab
```
```
./ij -n 50 50 50 -difconv -a 10 -amg
```
```
./ij -n 50 50 50 -difconv -a 10 -amg -agg_nl 1
```
{% include qanda question='What do you observe? Order the solvers in the order of slowest to fastest solver for this problem!' answer='BiCGSTAB, GMRES and AMG with or without aggressive coarsening solve the problem. The order slowest to fastest for this problem is: GMRES(20), AMG, BiCGSTAB, AMG with aggressive coarsening.' %}

Let us solve the problem using structured multigrid solvers.
```
./struct -n 50 50 50 -a 10 -pfmg
```
```
./struct -n 50 50 50 -a 10 -pfmg -rap 1
```
```
./struct -n 50 50 50 -a 10 -pfmggmres
```
```
./struct -n 50 50 50 -a 10 -pfmggmres -rap 1
```

{% include qanda question='What do you observe? Which solver fails? What is the order of the remaining solvers in terms of number of iterations? Which solver is the fastest.' answer='The non-Galerkin version of PFMG as alone solver fails. The order from largest to least number of iterations is: Non-Galerkin PFMG-GMRES, PFMG, PFMG-GMRES. But PFMG alone solves the problem faster.' %}

We will now consider a two-dimensional problem with a rotated anisotropy on a rectangular domain.
Let us begin with a grid-aligned anisotropy.
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 0 -gmres -k 100 -iout 3
```
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 0 -bicgstab -iout 3
```
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 0 -amg -iout 3
```
{% include qanda question='What do you observe?' answer='The residual norms for all solvers improve, but only AMG converges within less than 1000 iterations.' %}

Now let us rotate the anisotropy by 45 degrees.
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 45 -amgbicgstab
```
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 45 -amggmres
```
```
./ij -rotate -n 300 300 -eps 0.01 -alpha 45 -amg
```

{% include qanda question='Does the result change? What is the order of the solvers?' answer='The order from slowest to fastest is: AMG, AMG-GMRES, AMG-BiCGSTAB.' %}

Let us now scale up the problem.
```
mpiexec -n 2 ./ij -P 2 1 -rotate -n 300 300 -eps 0.01 -alpha 45 -amggmres
```
```
mpiexec -n 4 ./ij -P 2 2 -rotate -n 300 300 -eps 0.01 -alpha 45 -amggmres
```
```
mpiexec -n 8 ./ij -P 4 2 -rotate -n 300 300 -eps 0.01 -alpha 45 -amggmres
```

{% include qanda question='How do the numbers of iterations change?' answer='They increase to 10 when running more than 1 process, but stay 10 all three parallel runs.' %}

Let us now rotate the anisotropy by 30 degrees.
```
mpiexec -n 8 ./ij -P 4 2 -rotate -n 300 300 -eps 0.01 -alpha 30 -amggmres
```
{% include qanda question='Is the convergence affected by the change in angle?' answer='This problem is harder. The number of iterations increases to 15.' %}

Let us now coarsen more aggressively.
```
mpiexec -n 8 ./ij -P 4 2 -rotate -n 300 300 -eps 0.01 -alpha 30 -amggmres -agg_nl 1
```
{% include qanda question='Does this improve convergence and time?' answer='No. Both get worse. The number of iterations increases to 34 and the time goes up.' %}

Let us investigate the operator complexities:
```
mpiexec -n 8 ./ij -P 4 2 -rotate -n 300 300 -eps 0.01 -alpha 30 -amggmres -iout 1
```
```
mpiexec -n 8 ./ij -P 4 2 -rotate -n 300 300 -eps 0.01 -alpha 30 -amggmres -agg_nl 1 -iout 1
```

{% include qanda question='What are the operator complexities and how large is the largest average number of nonzeroes per row (row avg) for both cases?' answer='The operator complexities are 3.2 and 1.3. The largest average number of nonzeroes per row are 36.3 and 27.5.' %}

Often using aggressive coarsening is not recommended for two-dimensional problems, which generally have less growth in the number of nonzeroes per row than three-dimensional problems.

## Out-Brief

We experimented with several Krylov solvers, GMRES, conjugate gradient and BiCGSTAB, and observed the effect of increasing the size of the Krylov space for restarted GMRES. We investigated why multigrid methods are preferable over generic solvers like conjugate gradient for large suitable PDE problems.
Additional improvements can be achieved when using them as preconditioners for Krylov solvers like conjugate gradient.
For unstructured multigrid solvers, it is important to keep complexities low, since large complexities lead to slow solve times and require much memory.
For structured problems, solvers that take advantage of the structure of the problem are more efficient than unstructured solvers.


### Further Reading

To learn more about algebraic multigrid, see
[An Introduction to Algebraic Multigrid](https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods/CiSE_2006_amg_220851.pdf)

More information on hypre , including documentation and further publications, can be found [here](http://www.llnl.gov/CASC/hypre)
