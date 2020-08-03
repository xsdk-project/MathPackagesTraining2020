---
layout: page-fullwidth
order: 8
title: "Nonlinear Solvers with PETSc"
subheadline: "--Insert Subheadline=="
teaser: "--Insert Teaser--"
permalink: "lessons/nonlinear_solvers_petsc/"
use_math: true
lesson: true
header:
 image_fullwidth: "xsdk_logo_wide-fs8.png"
---

## At a Glance

|**Questions**|**Objectives**|**Key Points**|
|1. Question 1?|Goal 1|Info 1|
|2. Question 2?|Goal 2|Info 2|
|3. Question 3?|Goal 3|Info 3|

**Note:** To run the application in this lesson
```
Insert quick-reference code here...
```

## Introduction

Blah blah blah.

## Other Stuff?

Blah blah blah.

## Hands-On: Solving the driven cavity problem with Newton's method

In the first set of examples, we will use (inexact) Newton methods to solve the driven cavity problem, SNES `ex19`.

### Example 1: Initial exploration and understanding PETSc options

Let's begin by running the `ex19` on a single MPI rank with some basic command line options.

```
./ex19 -snes_monitor -snes_converged_reason -da_grid_x 16 -da_grid_y 16 -da_refine 2 -lidvelocity 100 -grashof 1e2
```

You should see output similar to
```
lid velocity = 100., prandtl # = 1., grashof # = 100.
  0 SNES Function norm 7.681163231938e+02 
  1 SNES Function norm 6.582880149343e+02 
  2 SNES Function norm 5.294044874550e+02 
  3 SNES Function norm 3.775102116141e+02 
  4 SNES Function norm 3.047226778615e+02 
  5 SNES Function norm 2.599983722908e+00 
  6 SNES Function norm 9.427314747057e-03 
  7 SNES Function norm 5.212213461756e-08 
Nonlinear solve converged due to CONVERGED_FNORM_RELATIVE iterations 7
Number of SNES iterations = 7

```
The table below explains the options we have used:

|**Option Flag**|**Effect**|
|`-snes_monitor`| Show progress of the SNES solver|
|`-snes_converged_reason`| Print reason for SNES convergence or divergence|
|`-da_grid_x 16`| Set initial grid points in x direction to 16|
|`-da_grid_y 16`| Set initial grid poings in y direction to 16|
|`-da_refine 2`| Refine the initial grid 2 times before creation|
|`-lidvelocity 100`| Set dimensionless velocity of lid to 100|
|`-grashof 1e2`| Set Grashof number to 1e2|

An element of the PETSc design philosphy is extensive runtime customizability.
We can always use `-help` to enumerate and explain the various command-line options
available to a PETsc executable.
(Note that the help will be tailored to according to the set of options being specified.)

To see the details of how our SNES solver is configured, we can add `-snes_view`, which will
print information at the end of the run about the SNES object and the underlying KSP
(linear solvers) and PC (preconditioners) objects.

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">Example `-snes_view` output</h4></summary>
```
Nonlinear solve converged due to CONVERGED_FNORM_RELATIVE iterations 7
SNES Object: 1 MPI processes
  type: newtonls
  maximum iterations=50, maximum function evaluations=10000
  tolerances: relative=1e-08, absolute=1e-50, solution=1e-08
  total number of linear solver iterations=835
  total number of function evaluations=11
  norm schedule ALWAYS
  Jacobian is built using colored finite differences on a DMDA
  SNESLineSearch Object: 1 MPI processes
    type: bt
      interpolation: cubic
      alpha=1.000000e-04
    maxstep=1.000000e+08, minlambda=1.000000e-12
    tolerances: relative=1.000000e-08, absolute=1.000000e-15, lambda=1.000000e-08
    maximum iterations=40
  KSP Object: 1 MPI processes
    type: gmres
      restart=30, using Classical (unmodified) Gram-Schmidt Orthogonalization with no iterative refinement
      happy breakdown tolerance 1e-30
    maximum iterations=10000, initial guess is zero
    tolerances:  relative=1e-05, absolute=1e-50, divergence=10000.
    left preconditioning
    using PRECONDITIONED norm type for convergence test
  PC Object: 1 MPI processes
    type: ilu
      out-of-place factorization
      0 levels of fill
      tolerance for zero pivot 2.22045e-14
      matrix ordering: natural
      factor fill ratio given 1., needed 1.
        Factored matrix follows:
          Mat Object: 1 MPI processes
            type: seqaij
            rows=14884, cols=14884, bs=4
            package used to perform factorization: petsc
            total: nonzeros=293776, allocated nonzeros=293776
            total number of mallocs used during MatSetValues calls=0
              using I-node routines: found 3721 nodes, limit used is 5
    linear system matrix = precond matrix:
    Mat Object: 1 MPI processes
      type: seqaij
      rows=14884, cols=14884, bs=4
      total: nonzeros=293776, allocated nonzeros=293776
      total number of mallocs used during MatSetValues calls=0
        using I-node routines: found 3721 nodes, limit used is 5
```
</details>
</div>
{::options parse_block_html="false" /}

### Managing PETSc Options

PETSc offers a very large number of runtime options.
All can be set via command line, but can also be set from input files
and shell environment variables.

To facilitate readability, we'll put the command-line arguments common to the remaining
hands-on exercises in the `PETSC_OPTIONS` environment variable.
```
export PETSC_OPTIONS="-snes_monitor -snes_converged_reason -lidvelocity 100 -da_grid_x 16 -da_grid_y 16 -ksp_converged_reason -log_view :log.txt"
```
We've added `-ksp_converged_reason` to see how and when linear solver halts.

We've also added `-log_view` to write the PETSc performance logging info to a file, `log.txt`.
Such performance logs are full of useful information for understanding the performance of
a PETSc code, but we don't have time to explore them in this session.
(For those interested, see Chapter 13, "Profiling", of the 
[PETSc User Manual](https://www.mcs.anl.gov/petsc/petsc-current/docs/manual.pdf).)
Here, we will simply use the performance logs to find the overall wall-clock time via,
which we can quickly find by using the `grep` utility:
```
grep Time\ \(sec\): log.txt
```
(The first number returned is the total run time in seconds.)

### Example 2: Exact vs. Inexact Newton

The output from running `-snes_view` in the previous exercise shows us that PETSc defaults
to an inexact Newton method. To run with exact Newton (and to check the execution time), we
use `-pc_type lu`, which indicates to the KSP object (which controls the linear solver) that
the underlying preconditioner should be an full LU decomposition:
```
./ex19 -da_refine 2 -grashof 1e2 -pc_type lu
grep Time\ \(sec\): log.txt
```
(Remember, the above command assumes that you have set `PETSC_OPTIONS` as specified in the
preceding section.)

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">Sample output on my laptop (Dell XPS 13 with Intel Core i7-10710U CPU)</h4></summary>
```
rmills@encke:~/proj/petsc/src/snes/tutorials (master=)$ ./ex19 -da_refine 2 -grashof 1e2 -pc_type lu
lid velocity = 100., prandtl # = 1., grashof # = 100.
  0 SNES Function norm 7.681163231938e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  1 SNES Function norm 6.581690463182e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  2 SNES Function norm 5.291809327801e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  3 SNES Function norm 3.772079270664e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  4 SNES Function norm 3.040001036822e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  5 SNES Function norm 2.518761157519e+00 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  6 SNES Function norm 9.230363584762e-03 
  Linear solve converged due to CONVERGED_RTOL iterations 1
  7 SNES Function norm 6.155757710494e-09 
Nonlinear solve converged due to CONVERGED_FNORM_RELATIVE iterations 7
Number of SNES iterations = 7
rmills@encke:~/proj/petsc/src/snes/tutorials (master=)$ grep Time\ \(sec\): log.txt
Time (sec):           6.728e-01     1.000   6.728e-01
```
</details>
</div>
{::options parse_block_html="false" /}

The work required to solve the inner, linear interation so precisely is likely wasted.
Let's try using the default iterative solver with some different tolerances. Start with
```
./ex19 -da_refine 2 -grashof 1e2 -ksp_rtol 1e-8
```
and then try some larger values for relative convergence tolerance, `-ksp_rtol`.
Try `-ksp_rtol 1e-5` (the PETSc default) next, and try increasing it by an order of
magnitude each time.

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">What happens to the SNES iteration count? When does the SNES solve diverge?</h4></summary>
The SNES iteration count is 7 initially, then increases to 8 at a relative tolerance of 1e-3 for the linear solver, and then 10 at a tolerance of 1e-2. The SNES solve diverges when run with a linear solver tolerance of 1e-1.
</details>
</div>
{::options parse_block_html="false" /}

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">What yields the shortest execution time?</h4></summary>
On my laptop, the loosest tolerance I tried, `-ksp_rtol 1e-2`, turns out to be fastest, able
to solve the problem in 0.43 seconds. Though it requires more Newton iterations, it performs
far fewer linear solver iterations. Running with the default tolerance of 1e-5 requires 
0.60 seconds. A tolerance of 1e-8 is far too high, resulting in many linear solver iterations
and an execution time of over 1.2 seconds.
Using LU factorization turns out to not be too bad for this small problem (around 0.68 
seconds), but it is difficult for LU to scale up to large problems.
</details>
</div>
{::options parse_block_html="false" /}

### Example 3: Scaling up the grid size and running in parallel

Let's explore what happens as we scale up the grid size for our model problem.

For this exercise, we will run in parallel because experiments may take too long otherwise.
We will use a fixed number of MPI ranks, even though this number is really too large for
the smaller grids, to eliminate effects due to varying the size of the domains used by the
default parallel preconditioner (block Jacobi with ILU(0) applied on each block).
We also use BiCGStab `-ksp_type bcgs` instead of the default linear solver, GMRES(30), will
fail for some cases.

Using the linear solver defaults, increase the size of the grid (that is, decrease the
grid spacing) and observe what happens to iteration counts and execution times:
```
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -da_refine 2
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -da_refine 3
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -da_refine 4 
```

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">Sample output for `-da_refine 4` case</h4></summary>
```
$ mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -da_refine 4
lid velocity = 100., prandtl # = 1., grashof # = 100.
  0 SNES Function norm 1.545962539057e+03 
  Linear solve converged due to CONVERGED_RTOL iterations 125
  1 SNES Function norm 9.782056791818e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 128
  2 SNES Function norm 6.621936395441e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 389
  3 SNES Function norm 3.155672307430e+00 
  Linear solve converged due to CONVERGED_RTOL iterations 470
  4 SNES Function norm 8.129969608884e-03 
  Linear solve converged due to CONVERGED_RTOL iterations 425
  5 SNES Function norm 8.852310456001e-08 
Nonlinear solve converged due to CONVERGED_FNORM_RELATIVE iterations 5
```
</details>
</div>
{::options parse_block_html="false" /}

You should observe that the Newton solver shows "mesh independence" -- that is, as we
refine the grid spacing, we see roughly the same convergence behavior for the Newton
iterates.
This is **not** true, however, for the linear solver, which shows unsustainable growth in
the number of iterations it requires.

What happens if we employ a Newton-Krylov-multigrid method?
Add `-pc_type mg` to use a geometric multigrid preconditioner (defaults to a V-cycle, but
check out the `-help` output to see how to use other types):

```
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -pc_type mg -da_refine 2
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -pc_type mg -da_refine 3
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -pc_type mg -da_refine 4 
```

{::options parse_block_html="true" /}
<div style="border: solid #8B8B8B 2px; padding: 10px;">
<details>
<summary><h4 style="margin: 0 0 0 0; display: inline">Sample output for `-pc_type mg -da_refine 4` case</h4></summary>
```
mpirun -n 12 ./ex19 -ksp_type bcgs -grashof 1e2 -pc_type mg -da_refine 4
lid velocity = 100., prandtl # = 1., grashof # = 100.
  0 SNES Function norm 1.545962539057e+03 
  Linear solve converged due to CONVERGED_RTOL iterations 6
  1 SNES Function norm 9.778196290981e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 6
  2 SNES Function norm 6.609659458090e+02 
  Linear solve converged due to CONVERGED_RTOL iterations 7
  3 SNES Function norm 2.791922927549e+00 
  Linear solve converged due to CONVERGED_RTOL iterations 6
  4 SNES Function norm 4.973591997243e-03 
  Linear solve converged due to CONVERGED_RTOL iterations 6
  5 SNES Function norm 3.241555827567e-05 
  Linear solve converged due to CONVERGED_RTOL iterations 9
  6 SNES Function norm 9.883136583477e-10 
Nonlinear solve converged due to CONVERGED_FNORM_RELATIVE iterations 6
```
</details>
</div>
{::options parse_block_html="false" /}

The takeaway here is that the combination of the fast convergence of a globalized
Newton method and a multigrid preconditioner for the inner, linear solve can be a powerful
and highly scalable solver.
## Take-Away Messages

* Important
* Items
* To
* Remember

## Further Reading

- [PETSc manual](https://www.mcs.anl.gov/petsc/petsc-current/docs/manual.pdf)
- [PETSc/TAO website](https://www.mcs.anl.gov/petsc)
- More links?

## Previous Nonlinear Solvers Lectures
- [ATPESC 2019](https://xsdk-project.github.io/MathPackagesTraining/lessons/time_integrators/sundials)
- [ATPESC 2018](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/lessons/time_integrators/)
