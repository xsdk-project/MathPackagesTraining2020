---
layout: page
show_meta: false
title: "Session Synopses"
subheadline: "More details about each session"
header:
   image_fullwidth: "amrex_warpx-fs8.png"
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

In this lecture we discuss the role and impact of high order, adaptive, and
flexible time integration libraries in solution accuracy and computational
efficiency of large-scale simulations.  Due to the wide variety of
backgrounds among ATPESC participants, we briefly discuss

* the location of time integrators in the HPC landscape, and their reliance on scalable nonlinear and linear solver libraries,
* the different categories of time integration methods (explicit/implicit/IMEX),
* the basic theoretical properties of time integration methods (order of accuracy, linear stability),
* the role of temporal adaptivity for improving accuracy and efficiency,
* an overview of DOE time integration packages.

We spend approximately half of the time period in lecture, followed by
hands-on exercises that examine stability, accuracy, temporal adaptivity,
and the role of problem-specific preconditioning.  All of the hands-on
exercises focus on time-dependent PDEs, and use the SUNDIALS' ARKODE
library for time integration, along with the AMReX library for spatial
semi-discretization.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Iterative Solvers & Preconditioners with MeuLu
### Iterative Solvers & Preconditioners with MeuLu

In this session, you will learn about linear solvers and preconditioners
available in the Trilinos project.  We will focus on Krylov solvers such
as conjugate gradients (CG) and generalized minimum residual (GMRES); simple
preconditioners like Jacobi, Gauss-Seidel, and Chebyshev polynomials; and
scalable aggregation-based algebraic multigrid preconditioning.  The two
hands-on lessons will give you an opportunity to run a variety of stand-alone
examples that demonstrate some of the many Trilinos solver capabilities on a
model linear problem.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Iterative Solvers & Preconditioners with Hypre
### Iterative Solvers & Preconditioners with Hypre

We will present the basic concepts of iterative linear solvers with focus on
Krylov solvers, including the generalized minimum residual method (GMRES),
preconditioning and algebraic multigrid (AMG) methods. We will provide a brief
description of the high performance linear solvers library hypre, its
interfaces and its most used multigrid solvers, BoomerAMG and PFMG, including
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
