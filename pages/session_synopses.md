---
layout: page
show_meta: false
title: "Session Synopses"
subheadline: "More details about each session"
permalink: "/session_synopses/"
---

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Structured Discretization
### Structured Discretization with AMReX

Block-structured adaptive mesh refinement (AMR) provides a natural framework
in which to focus computing power on the most critical parts of the problem in
the most computationally efficient way possible.  AMReX supports the development
of block-structured AMR algorithms for solving systems of partial differential
equations (PDE's) and other algorithms that require structured mesh and/or
particle discretizations.   We will begin with an overview of block-structured
AMR, including several different time-stepping strategies, and then discuss the
features of AMReX we might want to use to solve a multiphysics problem on
machines from laptops to supercomputers.  Hands-on exercises will include passive
scalar advection with time-dependent adaptivity,  the use of native linear
solvers to impose incompressibility on a flow around obstacles, and
"AMReX-Pachinko", which demonstrates the interaction of particles with objects.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Unstructured Discretization
### Unstructured Discretization with MFEM and PUMI
[Slides - Part 1](https://drive.google.com/file/d/1r4Q6-xyEinXaV9aub5gEB0yUMyc4GuDA/view?usp=sharing)<br>[Slides - Part 2](https://drive.google.com/file/d/1Nys2IqY7Q7vfeEP3uLvBBv8rJROW-W6l/view?usp=sharing)

Unstructured meshes can yield required levels of accuracy using fewer degrees of
freedom at the cost of more complex parallel data structures and algorithms. To
support the ability of application code developers to take advantage of unstructured
meshes, FASTMath develops core tools to support the development of unstructured
mesh simulation capabilities. This lecture will first introduce the highly extendible
MFEM high order finite element solver library and then overview the PUMI unstructured
mesh tools developed to support mesh adaptation, load balancing and PIC calculations. 

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Nonlinear Solvers
### Nonlinear Solvers with PETSc
[Slides](https://drive.google.com/file/d/1JxVnZ4fBpYnN2xgBu0RkOQHRZHR-zxbB/view?usp=sharing)

We will begin with a quick overview of iterative solvers for nonlinear systems,
and then take a deeper look into Newton-Krylov methods and how to use them via
the PETSc Scalable Nonlinear Equation Solvers (SNES) component. We will do
some hands-on exploration with a classic computational fluid dynamics benchmark,
the lid-driven cavity problem. We will end by looking at how nonlinear composition
and preconditioning can be used to construct a wide array of nonlinear solvers from
the algorithmic building blocks in SNES, and demonstrate how these techniques can
handle particularly difficult nonlinearities.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Time Integration
### Time Integration with SUNDIALS
[Slides](https://drive.google.com/file/d/1moq42mWch96fhNH9EADURhv0JHXECvUE/view?usp=sharing)

In this lecture we will discuss the role and impact of high order, adaptive, and
flexible time integration libraries in solution accuracy and computational
efficiency of large-scale simulations.  Due to the wide variety of
backgrounds among ATPESC participants, we will briefly discuss

* the location of time integrators in the HPC landscape, and their reliance on scalable nonlinear and linear solver libraries,
* the different categories of time integration methods (explicit/implicit/IMEX),
* the basic theoretical properties of time integration methods (order of accuracy, linear stability),
* the role of temporal adaptivity for improving accuracy and efficiency,
* an overview of DOE time integration packages.

We will spend approximately half of the time period in lecture, followed by
hands-on exercises that examine stability, accuracy, temporal adaptivity,
and the role of problem-specific preconditioning.  All of the hands-on
exercises focus on time-dependent PDEs, and use the SUNDIALS' ARKODE
library for time integration, along with the AMReX library for spatial
semi-discretization.


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Iterative Solvers & Preconditioners with MueLu
### Iterative Solvers & Preconditioners with MueLu
[Slides](https://drive.google.com/file/d/1kw0e4vAvVkt7OXiW5-suKztvNRIMfwc5/view?usp=sharing)

In this session, attendees will learn about linear solvers and preconditioners
available in the Trilinos project.  We will focus on Krylov solvers such
as conjugate gradients (CG) and generalized minimum residual (GMRES); simple
preconditioners like Jacobi, Gauss-Seidel, and Chebyshev polynomials; and
scalable aggregation-based algebraic multigrid preconditioning.  The two
hands-on lessons will provide an opportunity to run a variety of stand-alone
examples that demonstrate some of the many Trilinos solver capabilities on a
model linear problem.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Iterative Solvers & Preconditioners with Hypre
### Iterative Solvers & Preconditioners with Hypre
[Slides](https://drive.google.com/file/d/1gpLnYpRflYPTyBuRfV_kZtSzE-nfy2S2/view?usp=sharing)

This session will present the basic concepts of iterative linear solvers with focus on
Krylov solvers, including the generalized minimum residual method (GMRES),
preconditioning and algebraic multigrid (AMG) methods. We will provide a brief
description of the high performance linear solvers library hypre, its
interfaces, and its most used multigrid solvers, BoomerAMG and PFMG, including
a brief discussion of the effect of their data structures on performance.
The lesson includes hands-on examples with structured and unstructured solvers
from the hypre library applied to several test problems.
 

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Optimization
### Optimization with PETSc/Tao

This lecture will provide an introduction to numerical optimization with a
theoretical focus on simulation-based problems. We will introduce the user
interfaces for the Toolkit for Advanced Optimization (Tao) package within
the PETSc library and exercise several gradient-based algorithms on scalable
synthetic test problems. We will observe and discuss the relative convergence
of different classes of algorithms and sensitivity analysis methods in a
parallel environment.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Direct Solvers
### Direct Solvers with SuperLU and Strumpack

Direct Solvers are presented in three different time slots, each with a slightly
different emphasis...

* Session 1 (10:30am-11:30am):
  * Sparse direct solvers (both SuperLU and Strumpack), 30 minutes  (Sherry)
  * Low rank approximation techniques in Strumpack, 15 minutes (Pieter)
  * SuperLU hands-on demo, 15 minutes (Sherry)

* Session 2 (11:45am-12:45pm):
  * Sparse direct solvers (both SuperLU and Strumpack), 30 minutes  (Sherry)
  * Low rank approximation techniques in Strumpack, 15 minutes (Pieter)
  * Strumpack hands-on demo, 15 minutes (Pieter)

* Session 4 (3:40pm - 4:30pm):
  * Sparse direct solvers (both SuperLU and Strumpack), 30 minutes  (Sherry)
  * Low rank approximation techniques in Strumpack, 15 minutes (Pieter)
  * Q&A.  (Sherry, Pieter)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Working with Numerical Packages in Practice
### Working with Numerical Packages in Practice

Developing high-quality, large-scale scientific computing applications in science and
engineering involves expertise in many areas. Typically, no one person or group has
all of the essential expertise and skills. Numerical software libraries and packages
are a key way we share capability and know-how. Learning to leverage numerical
packages to address new scientific computing challenges is part of becoming a member of
the scientific computing community. In this wrap-up session of the day, we
breifly discuss key tradeoffs in using numerical packages in practice.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Panel - Contributing to the Numerical Package Community
### Panel - Contributing to the Numerical Package Community

This will be a 45 minute panel question and answer period for ATPESC learners to ask
questions about working with numerical package and the community of numerical package
developers. If you have question(s) you know you would like to ask, we encourage attendees
to submit questions *ahead* of time via the
[submission form](https://docs.google.com/forms/d/e/1FAIpQLScFAHguSG6m7H9lfjfSTSyOm1RZc1Mcc1N9aEAUyx4GTXpDhA/viewform?usp=sf_link).
However, we expect there will also be ample opportunty to indicate your desire to ask
questions via the main (Ampitheater) [slack channel](https://join.slack.com/share/zt-g2iz7j9z-DlNMA~iDqAg9Q4AbaU6Lmg),
and then you may be called upon to un-mute and ask your question.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### SME Speed Dating OPTIONAL ACTIVITY
### SME Speed Dating OPTIONAL ACTIVITY

This is an opportunity for you to meet and talk (1-on-1 or sometimes 2-on-1) with subject matter experts
(SMEs) about their work and numerical packages they support. Each *speed date* will be a 20 minute Zoom
meeting where you will be un-muted and able to have a conversation with an SME. Attendees may select up to
3 SMEs they would like to meet using
[this form](https://docs.google.com/forms/d/e/1FAIpQLSe73POCve2GDFeE5n-07tODaCNsZQlz_v7sS8qUVRvkc2FuaA/viewform?usp=sf_link)
Requests will be accomodated on a first-come, first-served basis until all available slots are taken.
So, be sure to make your selections early in the day and no later than the end of the afternoon break,
3:40 PM CDT.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
