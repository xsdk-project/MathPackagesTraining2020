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
|How does the choice of explicit,<br>implicit or IMEX method impact step size?|Compare performance of explicit,<br>implicit and IMEX methods at step<br>sizes near the stability limit.|The time integration type must<br>be chosen to match the problem.|
|What is the impact of an<br>adaptive time integrator?|Compare fixed and adaptive time<br>integration techniques.|Adaptive temporal integration can<br>provide robust and reliable solutions at a fraction of the cost.|
|How does time integration<br>order impact cost?|Observe impact of order<br>on time to solution<br>and number of steps.|In well-designed packages, changing<br>integration order is simple, allowing investigation of<br>optimal methods for a given problem.|
|How does the type of nonlinear solver<br>affect robustness/scalability|Compare Newton and accelerated fixed-point nonlinear<br>solvers for implicit and IMEX time integration methods.|Newton methods require more work-per step,<br>but may be necessary for stiff problems|
|What is the role and benefit of preconditioning?|Compare implicit and IMEX time integration<br>methods both with and without preconditioning.|Preconditioning may be overkill for small/simple problems,<br>but is critical for scalability.|

**Note:** To begin this lesson...

```bash
cd {{site.handson_root}}/time_integrators/sundials
make
source source_cooley_plotfile_tools.sh
```

## The problem being solved

The example applications here ([HandsOn1.cpp][3], [HandsOn2.cpp][4]
and [HandsOn3.cpp][5]) use a finite volume spatial discretization from
[AMReX][2] and the ODE solvers from [SUNDIALS][1], specifically
SUNDIALS' ARKode package for one-step time integration methods, to
demonstrate the use of [SUNDIALS][1] in both serial and parallel for
more robust and flexible control over _time integration_
(e.g. discretization in time) of PDEs.

These applications have been designed to solve a scalar-valued
advection-diffusion equation for chemical transport in 2 dimensions:

$$\frac{\partial u}{\partial t} + \vec{a} \cdot \nabla u -  \nabla \cdot ( D \nabla u ) = 0$$

where $$u = u(t,x,y)$$ is the chemical concentration, $$\vec{a}$$ is
the advection vector, $$D$$ is a diagonal matrix containing
anisotropic diffusion coefficients, and $$u(t=0,x,y)=u_0(x,y)$$ is a
given initial condition.  The spatial domain is $$(x,y) \in
[-1,1]^2$$, and the time domain is $$t \in (0,10^4]$$.

Here, all the runs solve a problem on a periodic, cell-centered,
uniform mesh with an initial 'bump':

$$u_0(x,y) = \frac{10}{\sqrt{2\pi}} e^{-50(x^2+y^2)}$$

Snapshots of the solution for advection vector $$\vec{a}=\left[\begin{array}{ll} 0.0005 & 0.00025\end{array}\right]$$ and
diffusion coefficient matrix $$D = \left[\begin{array}{cc} 10^{-6} & 0 \\ 0 & 10^{-6}\end{array}\right]$$ at the
times $$t = \left\{0, 1000, 2000, 3000\right\}$$ are shown in Figures 1-4 below:

|Figure 1|Figure 2|Figure 3|Figure 4|
|:---:|:---:|:---:|:---:|
|[<img src="advection-diffusion-u0.png" width="400">](advection-diffusion-u0.png)|[<img src="advection-diffusion-u1000.png" width="400">](advection-diffusion-u1000.png)|[<img src="advection-diffusion-u2000.png" width="400">](advection-diffusion-u2000.png)|[<img src="advection-diffusion-u3000.png" width="400">](advection-diffusion-u3000.png)|

We will break apart our investigation of this problem into the following three phases:

1. Explicit time integration (`HandsOn1.exe`)

(lunch break)

2. Implicit / IMEX time integration (`HandsOn2.exe`)

3. Preconditioning (`HandsOn3.exe`)


### Getting Help

You can get help on all the command-line options to these applications
with the `help=1` argument for any of these executables, e.g.

```
./HandsOn1.exe help=1
MPI initialized with 1 MPI processes
AMReX (19.07) initialized

Usage: HandsOn1.exe [fname] [options]
Options:
  help=1
    Print this help message and exit.
  plot_int=<int>
    enable (1) or disable (0) plots [default=0].
  arkode_order=<int>
    ARKStep method order [default=4].
  fixed_dt=<float>
    use a fixed time step size (if value > 0.0) [default=-1.0].
  rtol=<float>
    relative tolerance for time step adaptivity [default=1e-4].
  atol=<float>
    absolute tolerance for time step adaptivity [default=1e-9].
  tfinal=<float>
    final integration time [default=1e4].
  dtout=<float>
    time between outputs [default=tfinal].
  max_steps=<int>
    maximum number of internal steps between outputs [default=10000].
  write_diag=<int>
    output ARKStep time step adaptivity diagnostics to a file [default=1].
  n_cell=<int>
    number of cells on each side of the square domain [default=128].
  max_grid_size=<int>
    max size of boxes in box array [default=64].
  advCoeffx=<float>
    advection speed in the x-direction [default=5e-4].
  advCoeffy=<float>
    advection speed in the y-direction [default=2.5e-4].
  diffCoeffx=<float>
    diffusion coefficient in the x-direction [default=1e-6].
  diffCoeffy=<float>
    diffusion coefficient in the y-direction [default=1e-6].

If a file name 'fname' is provided, it will be parsed for each of the above
options.  If an option is specified in both the input file and on the
command line, then the command line option takes precedence.
```


## Hands-on lesson 1 -- Explicit time integration (`HandsOn1.exe`)

This lesson will explore the following topics:

a. Problem specification -- vector wrapper and right-hand side
   functions

b. Fixed time-stepping (exploration of linear stability)

c. Adaptive time-stepping

d. Time integrator order of accuracy


### Source code (problem specification)

Open the files `shared/NVector_Multifab.h` and
`shared/NVector_Multifab.cpp` -- these provide a thin wrapper for the
native AMReX `MultiFab` data structure so that SUNDIALS can think of
it as a "vector," and perform standard algebraic operations on the
native AMReX data:

* clone a vector to create work arrays

* linear combination: $$\vec{z} \gets a\vec{x} + b\vec{y}$$

* fill with constant: $$z_i \gets c, \; i=0,\ldots,N-1$$

* componentwise multiplication: $$\vec{z} \gets \vec{x} .* \vec{y}$$

* vector scale: $$\vec{z} \gets c \vec{x}$$

* norm and inner-product computations: $$\|\vec{x}\|_\infty$$,
  $$\left<\vec{x},\vec{y}\right>$$, etc.

* ...

Now open the files `shared/Utilities.cpp` and `HandsOn1.cpp`.

Starting on line 147, the file `shared/Utilities.cpp` defines a
function
```C
int ComputeRhsAdvDiff(Real t, N_Vector nv_sol, N_Vector nv_rhs, void* data)
```
that computes the problem-defining ODE right-hand side function on the
`NVector_Multifab` data, $$f(t,u) = -\vec{a} \cdot \nabla u + \nabla
\cdot ( D \nabla u )$$.

The file `HandsOn1.cpp` does a number of standard tasks:

1. Creates and fills a `NVector_Multifab` for the initial conditions,
   $$u_0(x,y)$$ vector (in the function `DoProblem()`, starting on
   line 305)

2. Creates the time integrator memory structure, and sets desired
   options (in the function `ComputeSolutionARK()`, starting on line
   36) -- here, the integrator is handed both the initial condition
   vector $$u_0(x,y)$$ and the ODE right-hand side function
   $$f(t,u)$$.

3. Evolves the problem over a series of time sub-intervals, storing
   the solutions as requested.

4. Reports the overall solver statistics and cleans up.


### Linear stability

Run the first hands-on code using its default parameters (note that
this uses a mesh size of $$128^2$$ and fixed time step size of 5.0),
```bash
./HandsOn1.exe inputs-1
```
and compare the final result against a stored reference solution (on a
$$128^2$$ grid),
```bash
fcompare.gnu.ex plt00001/ reference_solution/
```
Notice that the computed solution error is rather small.

Now re-run this hands-on code using a larger time step size of 100.0,
```bash
./HandsOn1.exe inputs-1 fixed_dt=100.0
```
_see how much faster the code ran!_  However, now check the accuracy
of the computed solution,
```bash
fcompare.gnu.ex plt00001/ reference_solution/
```
and note the reported error of $$10^{98}$$.

{% include qanda
    question='What do you think happened?'
    answer='At this mesh size, the explicit algorithm is unstable for
    a time step size of 100, but is stable for a time step size of 5.' %}

Run the code a few more times -- what is the largest stable time step
size that you can find?


### Temporal adaptivity

With this executable, we may switch to adaptive time-stepping (with
the default tolerances, $$rtol=10^{-4}$$ and $$atol=10^{-9}$$) by
specifying `fixed_dt=0`,
```bash
./HandsOn1.exe inputs-1 fixed_dt=0
fcompare.gnu.ex plt00001/ reference_solution/
```
_note how rapidly the executable finishes, providing a solution that
is both stable and accurate to within the specified tolerances!_

Run the accompanying Python script `process_ARKStep_diags.py` to view
some overall time adaptivity statistics and generate plots of the time
step size history,
```bash
./process_ARKStep_diags.py HandsOn1_diagnostics.txt
eog h_vs_iter.png
```
_notice how rapidly the adaptive time-stepper finds the CFL stability
limit_.  Also notice that the adaptivity algorithm periodically
attempts to increase the time step size to investigate whether this
stability limit has changed; however, the raw percentage of these
failed steps remains rather small.

Run the code a few more times with various values of `rtol` -- how
well does the adaptivity algorithm produce solutions within the
desired tolerances?  How do the number of time steps change as
different tolerances are requested?



### Integrator order and efficiency

ARKode defaults to a fourth-order accurate Runge--Kutta method,
but many others are included (with orders 2 through 8).  Alternate
orders of accuracy may be run with the `arkode_order` option, e.g.
```bash
./HandsOn1.exe inputs-1 fixed_dt=0 arkode_order=8
fcompare.gnu.ex plt00001/ reference_solution/
```
_note the dramatic decrease in overall time steps (457 vs 258), but
the accompanying increase in total RHS evaluations (2875 vs 3773)._
Although higher-order methods may indeed utilize larger step sizes
(both for accuracy and frequently stability), those come at
the cost of increased work per step.

Run the code a few more times with various values of `arkode_order`
for a fixed value of `rtol` -- what is the most "efficient" overall
method for this problem at this tolerance?



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
  `ComputeRhsAdv()` and `ComputeRhsDiff()` as an IMEX splitting of the
  ODE right-hand side.  By default, the problem is run in
  fully-implicit mode.

* When using the default inexact Newton nonlinear solver for implicit
  stage calculations, this creates and attaches an un-preconditioned
  GMRES iterative linear solver for solution of each Newton linear
  system.

* Or if requested, it creates and attaches an accelerated
  fixed-point nonlinear solver for implicit stage calculations.


### Linear stability revisited

Run the second hands-on code using its default parameters (note that
this also uses a mesh size of $$128^2$$ and fixed time step size of 5.0),
```bash
./HandsOn2.exe inputs-2
fcompare.gnu.ex plt00001/ reference_solution/
```
_note that this takes significantly longer than `HandsOn1.exe` with
the same time step size_

Now re-run using the larger time step size of 100.0,
```bash
./HandsOn2.exe inputs-2 fixed_dt=100.0
fcompare.gnu.ex plt00001/ reference_solution/
```
_again this version runs much more quickly, but now the results are usable!_

{% include qanda
    question='What do you think happened?'
    answer='This algorithm is fully-implicit (and in fact, it is
    A-stable), so linear instability was not a problem.' %}

Run the code a few more times with larger time step sizes, checking
the overall solution error each time -- can you find an unstable step
size?  Are there step sizes where the code may be stable, but are
so large that the nonlinear and/or linear solver fails to converge?



### Temporal adaptivity revisited

As with the previous hands-on exercise, we may switch to adaptive
time-stepping (with the default tolerances, $$rtol=10^{-4}$$ and
$$atol=10^{-9}$$) by specifying `fixed_dt=0`,
```bash
./HandsOn2.exe inputs-2 fixed_dt=0
```
Compute the solution error, and determine the adaptive time-stepping
statistics as before,
```bash
fcompare.gnu.ex plt00001/ reference_solution/
./process_ARKStep_diags.py HandsOn2_diagnostics.txt
```
How does that average step size for this tolerance compare against the
average step size of `HandsOn1.exe` for the same tolerances?

{% include qanda
    question='Open the plot `h_vs_iter.png` -- why do the time steps
    gradually increase throughout the simulation?'
    answer='The solution becomes smoother and decays toward zero as
    time goes on, making the initial guesses for each Newton and GMRES
    iteration more accurate, and the systems easier to solve, so
    ARKode gradually increases the step size as it is able.' %}

Run the code a few more times with various values of `rtol` -- how
well does the adaptivity algorithm produce solutions within the
desired tolerances?  How do the number of time steps change as
different tolerances are requested?  Is this algorithm more useful
than the fully explicit approach when loose tolerances (e.g.,
`rtol=1e-1`) are requested?


### Nonlinear solvers

As mentioned above, `HandsOn2.exe` defaults to solving implicit stages
using an inexact Newton nonlinear solver.  We may switch this
nonlinear solver algorithm to an accelerated fixed-point nonlinear
solver (with the default acceleration subspace size, `nls_fp_iter=5`)
by specifying `nls_method=1`,
```bash
./HandsOn2.exe inputs-2 nls_method=1 fixed_dt=0
fcompare.gnu.ex plt00001/ reference_solution/
```
How do the total number of implicit RHS function calls, solution
accuracy, number of time steps, and total runtime compare against an
identical run using the inexact Newton nonlinear solver?

{% include qanda
    question='Why is it that the total number of RHS function calls is
    no longer an ideal predictor of overall solver performance?'
    answer='Since the inexact Newton and accelerated fixed-point
    solvers use different internal algorithms (linear algebra, vs
    "acceleration"), the per-iteration costs of these methods vary
    substantially.' %}

Run the code a few more times with various values of `nls_fp_acc` to
determine whether there is a more 'optimal' value of the acceleration
subspace size for this problem.



### IMEX partitioning

By default, `HandsOn2.exe` uses a fully implicit formulation of the
problem.  However, this can instead be run with the advection terms
$$\vec{a} \cdot \nabla u$$ treated explicitly by specifying
`rhs_adv=2`,
```bash
./HandsOn2.exe inputs-2 rhs_adv=2
fcompare.gnu.ex plt00001/ reference_solution/
```
For comparison, run an identical test but with fully-implicit
treatment,
```bash
./HandsOn2.exe inputs-2
fcompare.gnu.ex plt00001/ reference_solution/
```
Do you notice any efficiency or accuracy differences between fully
implicit and IMEX formulations with these fixed time-step tests?

{% include qanda
    question='Why does ARKode report such significant differences in
    the number of explicit vs implicit RHS function evaluations?'
    answer='Since the explicit portion need only be computed once per
    stage, but the implicit portion must be repeatedly called at each
    stage during the nonlinear solver algorithm, we should expect
    ARK-IMEX methods to always evalute `Fi` more often than `Fe`.' %}

Now that we again have an explicit portion of the problem, we should
expect the time step size to be CFL-limited.  Run the code a few times
with various time step sizes, checking the overall solution error each
time -- can you find an unstable step size?

{% include qanda
    question='Why is the stability limit larger than for
    `HandsOn1.exe`?'
    answer='Since diffusion is now treated implicitly, the CFL-limited
    step size is now determined only by the advection terms.  As these
    are qualitatively different than the diffusion terms, we should
    expect different stability limitations.' %}



## Hands-on lesson 3 -- Preconditioning (`HandsOn3.exe`)

This lesson will explore the following topics:

a. Preconditioner specification

b. Performance for IMEX time integrators

c. Performance for fully implicit time integrators



### Source code (preconditioner specification)

Open the files `shared/Utilities.cpp` and `HandsOn3.cpp`.

In `shared/Utilities.cpp`, focus on the two routines
`precondition_setup` and `precondition_solve` starting on line 322.
These routines employ a scalable geometric multigrid solver for the
diffusion portion of the problem, $$\nabla \cdot ( D \nabla u )$$,
i.e., this should be a perfect preconditioner when running in IMEX
mode, or as an approximate preconditioner when running a fully
implicit formulation of the problem.  The file `HandsOn2.cpp` is
nearly identical to the previous versions (with relevant changes
indicated by the comment `***** UPDATED FROM HandsOn2 *****`), except
that:

* when creating the GMRES linear solver, it can configure GMRES
  to use left preconditioning (if requested), and

* if preconditioning is requested, it attaches the
  `precondition_setup` and `precondition_solve` routines to the time
  integrator.

Also, the default run parameters for `HandsOn3.exe` differ somewhat
from before:

* it defaults to adaptive time-stepping (with the same default
  tolerances)

* it defaults to IMEX mode, with advection treated explicitly

* it defaults to using the preconditioner.


### Performance with IMEX integration

Run `HandsOn3.exe` using the default parameters,
```bash
./HandsOn3.exe inputs-3
```
and again with preconditioning disabled,
```bash
./HandsOn3.exe inputs-3 use_preconditioner=0
```
_note that the preconditioned version takes longer to run on this
coarse problem, but shows significant improvements in the overall
number of linear solver iterations._

{% include qanda
    question='Given that the above test resulted in a _slower_ code
    when using preconditioning, then why is preconditioning used in
    large-scale simulation?'
    answer='We only ran this code on a very coarse problem, where the
    un-preconditioned GMRES solver proved "sufficient" for solving the
    Newton linear systems; however at larger scales the linear system
    becomes "ill-conditioned," requiring a preconditioner for
    convergence.  Related -- the preconditioned solver should be
    algorithmically scalable, so at some point we should expect the
    preconditioned version to out-perform the unpreconditioned
    version.' %}


### Performance with fully implicit integration

Re-run `HandsOn3.exe` using a fully-implicit problem formulation,
```bash
./HandsOn3.exe inputs-3 rhs_adv=1
```
Recall that this preconditioner only 'preconditions' the diffusion
portion of the problem, so when run in a fully-implicit manner the
implicit advection terms are left un-preconditioned.  Is this
discrepancy noticeable when comparing the solver statistics (number of
time steps, total linear iterations, etc.)?

In the evening hands-on session (below), you can explore the
scalability and efficiency of both the un-preconditioned and
preconditioned versions of this hands-on lesson.



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

Each of the following tasks are independent of one another.  Choose
one to explore in detail during this evening session (or if
interested, you may do multiple).

1. Examine the explicit stability boundary for `HandsOn1.exe` as the
   mesh size `n_cell` is changed to 256 and 512.  Do the same for
   `HandsOn2.exe` when running in IMEX mode (with explicit advection).

2. Explore the weak scalability of the fully implicit versions of
   `HandsOn2.exe` and `HandsOn3.exe` from say 1..36 MPI tasks, using a
   base grid of $$128^2$$ per MPI task.  Produce a weak scaling plot
   with these results.

3. Add a simple 'reaction' term to the problem, e.g.

   $$\frac{\partial u}{\partial t} + \vec{a} \cdot \nabla u -  \nabla \cdot ( D \nabla u ) = -u^2$$

   You may add this to either the explicit or implicit portions of the
   right-hand side; how well does the existing preconditioner do after
   this is added?

When you are done, be sure to submit a [Show Your Work](https://goo.gl/forms/B7UFpBvEOJbC58oJ2)
using the hands-on activity name _Time Integrators Scalability_ and
upload evidence of your completed solutions.


### Further Reading

[ARKode Manual -- PDF](https://computation.llnl.gov/sites/default/files/public/ark_guide.pdf)

[ARKode Manual -- HTML](http://runge.math.smu.edu/arkode_dev/doc/guide/build/html/index.html)

[1]: https://computation.llnl.gov/projects/sundials
[2]: https://amrex-codes.github.io/amrex
[3]: https://github.com/AMReX-Codes/ATPESC-codes/blob/master/SUNDIALS%2BAMReX/HandsOn1.cpp
[4]: https://github.com/AMReX-Codes/ATPESC-codes/blob/master/SUNDIALS%2BAMReX/HandsOn2.cpp
[5]: https://github.com/AMReX-Codes/ATPESC-codes/blob/master/SUNDIALS%2BAMReX/HandsOn3.cpp
