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

## Hands-on Examples: Solving the driven cavity problem with Newton's method

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
