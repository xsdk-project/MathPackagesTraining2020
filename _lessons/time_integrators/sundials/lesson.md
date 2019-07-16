---
layout: page-fullwidth
title: "Time Integration & Non-Linear Solvers with SUNDIALS"
subheadline: "Role and Impact of Time Integrators in Solution Accuracy and Computational Efficiency"
permalink: "lessons/time_integrators/sundials"
use_math: true
youtube: "https://youtu.be/vAJ6kDf7Ifk"
answers_google_form: "https://docs.google.com/forms/d/e/1FAIpQLSepKOxuQseZ-PycSwocahehWLjdMzPg76pjvNyNZfGxX5vpNQ/viewform?usp=sf_link"
lesson: true
header:
 image_fullwidth: "theta.png"
---
## At a Glance

|Questions|Objectives|Key Points|
|How does the choice of<br>explicit, implicit or IMEX impact step size.|Compare performance of explicit<br>, implicit and IMEX methods at step<br>sizes near the stability limit.|Time integration considerations<br>play a role in time to solution.|
|What is the impact of an<br>adaptive time integrator?|Compare fixed and adaptive time<br>integration techniques.|The SUNDIALS package has robust<br>and flexible methods for time integration.|
|How does time integration<br>order impact cost?|Observe impact of order<br>on time to solution/flop<br>and number of steps.|In well-designed packages, changing<br>between methods does not require significant effort.|
|Observe quadratic convergence <br> of Newton's method| Observe mesh independent convergence <br> of Newton's method |||

**Note:** To begin this lesson...

```bash
cd {{site.handson_root}}/time_integrators/sundials
make
```

## The problem being solved

The example application here, [Advection-Diffusion.cpp][3] uses a finite volume spatial discretization from [AMReX][2]
and the ODE solvers from [SUNDIALS][1], specifically SUNDIALS' ARKode package for one-step time integration methods,
to demonstrate the use of [SUNDIALS][1] in both serial and parallel for more robust and flexible control over
_time integration_ (e.g. discretization in time) of PDEs.

The first application has been designed to solve a scalar-valued advection-diffusion equation for chemical transport in 2 dimensions:

$$\frac{\partial u}{\partial t} + \vec{a} \cdot \nabla u -  \nabla \cdot ( D \nabla u ) = 0$$

where $$u = u(t,x,y)$$ is the chemical concentration, $$\vec{a}$$ is the advection vector, $$D$$ is a diagonal matrix
containing anisotropic diffusion coefficients, and $$u(t=0,x,y)=u_0(x,y)$$ is a given initial condition.  The spatial
domain is $$(x,y) \in [-1,1]^2$$, and the time domain is $$t \in (0,10^4]$$.

Here, all the runs solve a problem on a periodic, cell-centered, uniform mesh with an initial 'bump':

$$u_0(x,y) = \frac{10}{\sqrt{2\pi}} e^{-50(x^2+y^2)}$$

Snapshots of the solution for advection vector $$\vec{a}=\left[\begin{array}{ll} 0.0005 & 0.00025\end{array}\right]$$ and
diffusion coefficient matrix $$D = \left[\begin{array}{cc} 10^{-6} & 0 \\ 0 & 10^{-6}\end{array}\right]$$ at the
times $$t = \left\{0, 1000, 2000, 3000\right\}$$ are shown in Figures 1-4 below:

|Figure 1|Figure 2|Figure 3|Figure 4|
|:---:|:---:|:---:|:---:|
|[<img src="advection-diffusion-u0.png" width="300">](advection-diffusion-u0.png)|[<img src="advection-diffusion-u1000.png" width="300">](advection-diffusion-u1000.png)|[<img src="advection-diffusion-u2000.png" width="300">](advection-diffusion-u2000.png)|[<img src="advection-diffusion-u3000.png" width="300">](advection-diffusion-u3000.png)|


We will break apart our investigation of this problem into the following three phases:

1. Explicit time integration (`HandsOn1.exe`):

(lunch break)

2. Implicit / IMEX time integration (`HandsOn2.exe`):

3. Preconditioning (`HandsOn3.exe`):


### Getting Help

You can get help on all the command-line options to this application
with the `--help` argument for any of these executables, e.g.
**(update these)**

```bash
./hands-on-1.exe  --help

Usage: ./HandsOn1.exe [options] ...
Options:
   -h, --help
	Print this help message and exit.
   -m <string>, --mesh <string>, current value: ../../../data/periodic-hexagon.mesh
	Mesh file to use.
   -p <int>, --problem <int>, current value: 0
	Problem setup to use. See options in velocity_function().
   -rs <int>, --refine-serial <int>, current value: 2
	Number of times to refine the mesh uniformly in serial.
   -rp <int>, --refine-parallel <int>, current value: 0
	Number of times to refine the mesh uniformly in parallel.
   -o <int>, --order <int>, current value: 3
	Order (degree) of the finite elements.
   -s <int>, --ode-solver <int>, current value: 4
	ODE solver: 1 - Forward Euler,
	            2 - RK2 SSP, 3 - RK3 SSP, 4 - RK4, 6 - RK6.
   -tf <double>, --t-final <double>, current value: 10
	Final time; start time is 0.
   -dt <double>, --time-step <double>, current value: 0.01
	Time step.
   -vis, --visualization, -no-vis, --no-visualization, current option: --visualization
	Enable or disable GLVis visualization.
   -visit, --visit-datafiles, -no-visit, --no-visit-datafiles, current option: --visit-datafiles
	Save data files for VisIt (visit.llnl.gov) visualization.
   -vs <int>, --visualization-steps <int>, current value: 50
	Visualize every n-th timestep.
   -usestep, --usestep, -no-step, --no-step, current option: --usestep
	Use the Step() or Run() method to solve the ODE system.
   -implicit, --implicit, -no-implicit, --no-implicit, current option: --no-implicit
	Use or not an implicit method in ARKode to solve the ODE system.
```


## Hands-on lesson 1 -- Explicit time integration (`HandsOn1.exe`)

This lesson will explore the following topics:

a. Problem specification -- vector wrapper and right-hand side functions
b. Fixed time-stepping (exploration of linear stability)
c. Adaptive time-stepping
d. Time integrator order of accuracy


### Source code (problem specification)

Open the files `shared/NVector_Multifab.h` and `shared/NVector_Multifab.cpp` -- these provide a thin wrapper
for the native AMReX `MultiFab` data structure so that SUNDIALS can think of it as a "vector," and perform
standard algebraic operations on the natifve AMReX data:

* clone a vector to create work arrays
* $$\vec{z} \gets a\vec{x} + b\vec{y}$$
* $$z_i \gets c, \; i=0,\ldots,N-1$$
* $$\vec{z} \gets \vec{x} .* \vec{y}$$ (componentwise multiplication)
* $$\vec{z} \gets \vec{x} ./ \vec{y}$$ (componentwise division)
* $$\vec{z} \gets c \vec{x}$$
* ...

Now open the files `shared/Utilities.cpp` and `HandsOn1.cpp`.
Starting on line 147, the file `shared/Utilities.cpp` defines a
function
```C
int ComputeRhsAdvDiff(Real t, N_Vector nv_sol, N_Vector nv_rhs, void* data)
```
that computes the problem-defining ODE right-hand side function on the
`NVector_Multifab` data, $$f(t,u) = -\vec{a} \cdot \nabla u + \nabla
\cdot ( D \nabla u )$$.  The file `HandsOn1.cpp` does a number of
standard tasks:

1. Creates and fills a `NVector_Multifab` for the initial conditions,
   $$u_0(x,y)$$ vector (in the function `DoProblem()`, starting on line 254)
2. Creates the time integrator memory structure, and sets desired
   options (in the function `ComputeSolutionARK()`, starting on line
   36) -- here, the integrator is handed both the initial condition
   vector $$u_0(x,y)$$ and the ODE right-hand side function
   $$f(t,u)$$.
3. Evolves the problem over a series of time sub-intervals, storing
   the solutions as requested.
4. Reports the overall solver statistics and cleans up.



### Linear stability


### Temporal adaptivity


### Integrator order and efficiency



## Hands-on lesson 2 -- Implicit / IMEX time integration (`HandsOn2.exe`)

This lesson will explore the following topics:

a. Specification of algebraic solver algorithms (nonlinear and linear)
b. Fixed time-stepping (exploration of linear stability)
c. Adaptive time-stepping
d. Newton vs accelerated fixed-point nonlinear solver
e. Implicit-explicit partitioning


### Source code (specification of algebraic solvers)

Open the file `HandsOn2.cpp`.  This is nearly identical to
`HandsOn1.cpp` from the first lesson, with all relevant changes
indicated by the comment `***** UPDATED FROM HandsOn1 *****`.
Specific changes include:

* Specifies either `ComputeRhsAdvDiff()` as the *implicit*
  portion of the ODE, or specification of the two subset routines
  `ComputeRhsAdv()` and `ComputeRhsDiff()` as an IMEX splitting of teh
  ODE right-hand side.
* Creates and attaches either a GMRES iterative linear solver to the
  default inexact Newton nonlinear solver, or an accelerated
  fixed-point nonlinear solver, for the time integrator to use when
  solving implicit algebraic systems.


### Linear stability revisited


### Temporal adaptivity revisited


### Nonlinear solvers


### IMEX partitioning





## Hands-on lesson 3 -- Preconditioning (`HandsOn3.exe`)

This lesson will explore the following topics:

a. Preconditioner specification
b. Performance for IMEX time integrators
c. Performance for fully implicit time integrators



### Source code (specification of algebraic solvers)

Open the files `shared/Utilities.cpp` and `HandsOn3.cpp`.  In
`shared/Utilities.cpp` we will now focus on the two routines
`precondition_setup` and `precondition_solve` starting on line 322.
These routines employ a scalable geometric multigrid solver for the
diffusion portion of the problem, $$\nabla \cdot ( D \nabla u )$$,
i.e., this should be a perfect preconditioner when running in IMEX
mode, or as an approximate preconditioner when running a fully
implicit formulation of the problem.  The file `HandsOn2.cpp` is
nearly identical to the previous versions (with relevant changes
indicated by the comment `***** UPDATED FROM HandsOn2 *****`), except
that:

* when creating the GMRES linear solver, it indicates that GMRES
  should use left preconditioning, and
* attaches the `precondition_setup` and `precondition_solve` routines
  to the time integrator.


### Performance with IMEX integration


### Performance with fully implicit integration







## Out-Brief

We have used AMReX and SUNDIALS as a demonstration vehicle for
illustrating the value of robust time integration methods in numerical
algorithms. In particular, we have used the ARKode's `ARKStep` time
integration module from [SUNDIALS][1] to explore a range of questions
related to time integration and nonlinear solvers:

1. the benefits of _adaptive_ (vs _fixed_) time stepping for both
   performance and robustness of a simulation code,
2. the effects of the order of the time integration method on method
   efficiency,
3. the tradeoffs between more powerful (but costly) Newton-based
   nonlinear solvers and cheaper but more slowly-convergent
   fixed-point nonlinear solvers,
3. the increased cost but increased scalability offered through use of
   advanced preconditioning methods, and
4. the choice of IMEX partitioning in time discretization.

We note that our use of _adaptivity_ here was confined to the
_discretization_ of time. Other lessons here demonstrate the
advantages _adaptation_ can play in the _discretization_ of _space_
(e.g. meshing).

We further note that we have barely scratched the surface of linear
solver algorithms; while GMRES with geometric multigrid
preconditioning remain top choices for large-scale applications, other
lessons here will focus on alternatives that can work even when these
methods fail.

Finally, it is worth reminding the learner that the application
demonstrated here can be run on much larger spatial meshes and
parallel architectures than those tested here.

----

## Evening Hands On Session

Run the two examples with a different number of levels of refinement using `-rs n` and the `-log_view` option introduced above to explore the scalability of the algorithms. For example

```bash
PETSC_OPTIONS="-ts_adapt_monitor no -ts_type arkimex -ts_monitor :/dev/null -log_view " ./elasticity-snes -rs 2 -no-vis
```

then again

```bash
PETSC_OPTIONS="-ts_adapt_monitor no -ts_type arkimex -ts_monitor :/dev/null -log_view " mpiexec -n 4 ./elasticity-snes -rs 2 -no-vis
```

Try other combinations of levels of refinement and number of processes. Produce a small
_scaling_ plot showing scaling of algorithms from say 1..32 mpi ranks.

When you are done, be sure to submit a [Show Your Work](https://goo.gl/forms/B7UFpBvEOJbC58oJ2)
 using the hands-on activity name _Time Integrators Scalability_ and upload evidence of your completed solutions.

### Further Reading

[ARKode Manual -- PDF](https://computation.llnl.gov/sites/default/files/public/ark_guide.pdf)
[ARKode Manual -- HTML](http://runge.math.smu.edu/arkode_dev/doc/guide/build/html/index.html)

[1]: https://computation.llnl.gov/projects/sundials
[2]: https://amrex-codes.github.io/amrex
[3]: https://github.com/AMReX-Codes/ATPESC-codes/blob/master/SUNDIALS%2BAMReX/Advection-Diffusion/Advection-Diffusion.cpp
