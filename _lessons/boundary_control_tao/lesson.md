---
layout: page-fullwidth
title: "Poisson Boundary Control"
subheadline: "Numerical Optimization"
teaser: "Leveraging interoperability between PETSc/TAO and AMReX"
permalink: "lessons/boundary_control_tao/"
youtube: "https://www.youtube.com/channel/UCEkJLPAMOUsjC_RXGFcVq-A/videos"
use_math: true
lesson: true
header:
 image_fullwidth: "xsdk_logo_wide.png"
---

## At a Glance
<!-- (Expected # minutes to complete) %% temporarily omit -->

|Questions|Objectives|Key Points|
|1. What is PDE-constrained optimization?|Understand the basic principles|The PDE is imposed as an equality constraint for the optimization problem|
|2. What is the reduced-space formulation?|Separate the optimization and the PDE solution|The PDE states are removed from the optimization problem using the implicit function theorem|
|3. What is adjoint-based sensitivity analysis?|Compute gradients for functionals that depend on the solution of a PDE|The adjoint method can efficiently provide gradient information when the objective function relies on the solution of expensive PDEs|

**Note:** To run the application in this lesson
```
cd {{site.handson_root}}/boundary_control_tao
make
./main -tao_monitor -tao_view
```

## Brief Introduction to PDE-Constrained Optimization

PDE-constrained optimization algorithms seek to find the input variables or parameters (referred to as "control", "design" or "optimization" variables) that minimize (or maximize) a functional that depends on the solution of a partial differential equation (PDE). A general PDE-constrained optimization problem is stated as

$$
\min_{p, u} \quad f(p, u) \quad \text{subject to} \quad R(p, u) = 0,
$$

where $$p \in \mathbb{R}^n}$$ are the optimization variables, $$u \in \mathbb{R}^m$$ are the PDE states, $$f(p, u): \mathbb{R}^{n \times m} \rightarrow \mathbb{R}$$ is the objective function, and $$R(p, u): \mathbb{R}^{n \times m} \rightarrow \mathbb{R}^m$$ are the state equations that represent the discretized PDE.

The above optimization statement is called the "full-space" method for PDE-constrained optimization, where the PDE solution variables $$u$$ are solved simultaneously with the optimization variables $$p$$. Consequently, the size of the optimization problem is $$n + m$$.

In the "reduced-space" formulation, the PDe constraint is removed from the optimization problem using the implicit function theorem, such that

$$\min_p \quad f(p, u(p)),$$

where the state or solution variables $$u$$ are now expressed as an implicit function of the optimization variables $$p$$. In practice, this means that every evaluation of the objective function $$f(p, u(p))$$ at a new $$p$$ point requires a complete solution of the state equations $$R(p, u) = 0$$ in order to compute the solution $$u(p)$$ that corresponds to that $$p$$ point. Consequently, the function evaluation becomes significantly more expensive, at the trade-off that the size of the optimization problem shrinks to $$n$$.

The reduced-space formulation can also be re-written as 

$$\min_p \quad f(p, u(p)) \quad \text{governed by} \quad R(p, u) = 0,$$

where the "governed by" notation describes the governing equations that relate the solution variables $$u$$ to the optimization variables $$p$$, but are not imposed as constraints in the optimization problem.

In this lesson, we focus on gradient-based optimization methods -- methods that utilize information about the sensitivity of the objective function with respect to its inputs. We begin by exploring the optimality conditions for this class of algorithms as applied to the PDE-constrained problem.

## Optimality Conditions

For full-space PDE-constrained optimization, the first-order optimality conditions are derived first by forming the Lagrangian

$$\mathcal{L}(p, u, \lambda) = f(p, u) + \lambda^T R(p, u),$$

where $$\lambda \in \mathbb{R}^m$$ are the Lagrange multipliers associated with the PDE constraint. Differentiating the Lagrangian with respect to all of its inputs yields the first-order optimality conditions (also called the Karush-Kuhn-Tucker conditions) that must be satisfied by the optimal solution:

$$\nabla_p \mathcal{L} = \frac{\partial f}{\partial p} + \lambda^T \frac{\partial R}{\partial p} = 0,$$

$$\nabla_u \mathcal{L} = \frac{\partial f}{\partial u} + \lambda^T \frac{\partial R}{\partial u} = 0,$$

$$\nabla_\lambda \mathcal{L} = R(p, u) = 0.$$

Newton-type optimization algorithms apply the Newton's method to the first-order optimality conditions to produce the Karush-Kuhn-Tucker (KKT) system,

$$
\begin{bmatrix}
    \nabla_{pp}^2 \mathcal{L} && \nabla_{up}^2 \mathcal{L} && \frac{\partial R}{\partial p}^T \\
    \nabla_{pu}^2 \mathcal{L} && \nabla_{uu}^2 \mathcal{L} && \frac{\partial R}{\partial u}^T \\
    \frac{\partial R}{\partial p} && \frac{\partial R}{\partial u} && 0
\end{bmatrix}
\begin{pmatrix}
    \Delta p \\ \Delta u \\ \Delta \lambda
\end{pmatrix} = 
\begin{pmatrix}
    -\nabla_p \mathcal{L} \\ -\nabla_u \mathcal{L} \\ -R(p, u)
\end{pmatrix},
$$

which is solved at every Newton iteration to produce the step direction $$(\Delta p, \Delta u, \Delta \lambda)$$. The step is then globalized using a line search or a trust region framework in order to avoid stationary points that are not the minimum. This approach converges the PDE states simultaneously with the optimization variables. This means that the PDE solution 
and the optimization are tightly coupled and the PDE constraint is not satisfied at intermediate steps.

The reduced-space variant of the above problem solves the KKT system with the following steps:

1. Solve $$\nabla_\lambda \mathcal{L} = R(p, u) = 0$$ at each new $$p$$ for $$u(p)$$. This is called the "state solution", i.e.: calculating the PDE state at $$p$$.

2. Substitute $$p$$ and $$u(p)$$ into $$\nabla_u \mathcal{L}$$ amd solve $$\left( \frac{\partial R}{\partial u} \right)^T \lambda = -\frac{\partial f}{\partial u}$$ for $$\lambda(p, u)$$. This is called the "adjoint solution" and the Lagrange multipliers are called the adjoint variables in the reduced-space formulation.

3. Substitute $$p$$, $$u(p)$$ and $$\lambda(p, u)$$ into $$\nabla_p \mathcal{L}$$ and solve $$\nabla_{p}^2 \mathcal{L} \Delta p = -\nabla_p \mathcal{L}$$ for the step direction $$\Delta p$$.

Note that the reduced-space steps avoid the computation of second derivative information in $$\nabla_{pu}^2 \mathcal{L}$$ and $$\nabla_{uu}^2 \mathcal{L}$$. Additionally, the PDE solver and the optimization algorithm are decoupled from each other. This comes at the cost of performing a full PDE solution for every objective function evaluation.

## Using TAO

Toolkit for Advanced Optimization (TAO) is a package of optimization algorithms and tools developed at Argonne National Laboratory and distributed with the [Portable Extensible Toolkit for Scientific Computing (PETSc)][4] library. It is primarily intended for continuous gradient-based optimization, and supports PDE-constrained problems using the reduced-space formulation.

Below is a TAO main file template that can be adapted to any PDE-constrained problem:

```c
#include "petsc.h"

typedef struct {
  int n; /* number of optimization variables */
} AppCtx;

PetscErrorCode FormFunctionGradient(Tao tao, Vec P, PetscReal *fcn,Vec G,void *ptr)
{
  PetscErrorCode ierr;
  AppCtx *user = (AppCtx*)ptr;

  /* Compute objective function and store in fcn */
  /* 1. Compute the states U(P) for the given P vector (i.e.: solve the PDE) */
  /* 2. Use P and U(P) to compute the objective function */

  /* Compute gradient and store in G */
  /* 1. Solve the adjoint system for the adjoint variables lambda(P, U(P)) */
  /* 2. Compute the gradient G = \nabla_p f using P, U(P), lambda(P, U(P)) */

  return 0;
}

int main(int argc, char *argv[])
{
  PetscErrorCode ierr;
  AppCtx user;
  Tao tao;

  /* Initialize problem and set sizes */

  ierr = PetscInitialize( &argc, &argv,(char *)0,help );if (ierr) return ierr;
  ierr = VecCreateMPI(PETSC_COMM_WORLD, user.n, &X);CHKERRQ(ierr);
  ierr = VecSet(X, 0.0);CHKERRQ(ierr);

  ierr = TaoCreate(PETSC_COMM_WORLD, &tao);CHKERRQ(ierr);
  ierr = TaoSetType(tao, TAOBQNLS);CHKERRQ(ierr);
  ierr = TaoSetInitialVector(tao, X);CHKERRQ(ierr);
  ierr = TaoSetObjectiveAndGradientRoutine(tao, FormFunctionGradient, (void*) &user);CHKERRQ(ierr);
  ierr = TaoSetFromOptions(tao);CHKERRQ(ierr);
  ierr = TaoSolve(tao);CHKERRQ(ierr);

  ierr = VecDestroy(&X);CHKERRQ(ierr);
  ierr = TaoDestroy(&tao);CHKERRQ(ierr);
  ierr = PetscFinalize();
```

TAO calls the user-provided ``FormFunctionGradient()`` routine whenever the optimization algorithm needs to evaluate the objective and its gradient. The ``AppCtx`` structure contains any data the user has to preserve and propagate through for these computations.

## Example Problem: Boundary Control with the Poisson Equation

The inverse problem for the boundary control case is given as

$$\min_p \quad \frac{1}{2}\int_\Omega (u(p) - u_{targ})^2 d \Omega,$$

$$\text{governed by} \quad -\frac{\partial}{\partial x}\left(\rho \frac{\partial u}{\partial x} \right) + \mu u = h \quad \forall \; x \in (0, 1), \quad u(x=0) = p_1, \quad u(x=1) = p_2,$$

where $$u_{targ}$$ is a target solution that we want to recover by controlling the Dicihlet boundary terms $$p_1$$ and $$p_2$$. For simplicity, we set $$\rho = 1$$ and $$\mu = 0$$, and reduce the governing equation to the 1-D Poisson equation.

We apply a central finite difference stencil,

$$\frac{\partial u}{\partial x} \approx \frac{u(x+\delta) - 2u(x) + u(x-\delta)}{\delta^2},$$

to a 6-node discretization where nodes 0 and 6 are the Dirichlet boundaries. This yields the following linear system of equations in residual form:

$$
  R(p, u) = \begin{pmatrix}
      2u_1 - u_2 - \delta^2 h_1 - p_1 \\
      -u_1 + 2u_2 - u_3 - \delta^2 h_2 \\
      -u_2 + 2u_3 - u_4 - \delta^2 h_3 \\
      - u_3 + 2u_4 - \delta^2 h_4 - p_2
  \end{pmatrix} = 0.
$$

The Jacobians for this problem are

$$
\frac{\partial R}{\partial u} = \begin{bmatrix}
    2 && -1 && 0 && 0 \\
    -1 && 2 && -1 && 0 \\
    0 && -1 && 2 && -1 \\
    0 && 0 && -1 && 2
\end{bmatrix},
$$

and

$$
\frac{\partial R}{\partial p} = \begin{bmatrix}
    -1 && 0 \\
    0 && 0 \\
    0 && 0 \\
    0 && -1
\end{bmatrix}.
$$

The adjoint system for this problem is

$$\left(\frac{\partial R}{\partial u}\right)^T \lambda = -\frac{\partial f}{\partial u},$$

and the total derivative of the objective function w.r.t. the optimization variables is

$$\frac{d f}{d p} = \frac{\partial f}{\partial p} + \left(\frac{\partial R}{\partial p}\right)^T \lambda.$$

Note that the total derivative notation is $$\frac{d}{dp}(\cdot)$$ and includes indirect sensitivities that come through the governing equations. In this problem, the partial derivative of the objective w.r.t the optimization variables, denoted by $$\frac{\partial}{\partial p}(\cdot)$$, is zero because $$p$$ does not directly appear in the objective function.

### Implementation with AMReX



### Results



## Further Reading

[PETSc Manual](http://www.mcs.anl.gov/petsc/petsc-current/docs/manual.pdf)  
[TAO Manual](http://www.mcs.anl.gov/petsc/petsc-current/docs/tao_manual.pdf)
[AMReX Documentation](https://amrex-codes.github.io/amrex/docs_html/)

[1]: https://en.wikipedia.org/wiki/Quasi-Newton_method
[2]: https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm
[3]: https://books.google.com/books?id=VbHYoSyelFcC&dq=Nonlinear+Optimization+Nocedal&source=gbs_navlinks_s
[4]: http://www.mcs.anl.gov/petsc
[5]: https://amrex-codes.github.io/amrex/
