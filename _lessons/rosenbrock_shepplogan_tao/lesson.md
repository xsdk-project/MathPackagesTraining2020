---
layout: page-fullwidth
title: "Rosenbrock and Shepp-Logan with PETSc/TAO"
subheadline: "Numerical Optimization"
teaser: "A practical introduction to large-scale optimization"
permalink: "lessons/rosenbrock_shepplogan_tao/"
use_math: true
lesson: false
header:
 image_fullwidth: "xsdk_logo_wide-fs8.png"
header-includes:
  - \usepackage{algorithmic}
---

## At a Glance
<!-- (Expected # minutes to complete) %% temporarily omit -->

|Questions|Objectives|Key Points|
|1. What is optimization?|Understand the basic principles|Optimization seeks the inputs of a function that minimizes it|
|2. Why use gradient-based methods?|Learn about trade-offs in algorithm choice|Gradient-based methods find local minimums with the fewest number of function evaluations|
|3. How can we compute gradients?|Evaluate different sensitivity analysis methods|Applications should provide analytical gradients whenever they can|

**Note:** To run the application in this lesson
```
cd {{site.handson_root}}/rosenbrock_shepplogan_tao
make
./rosenbrock -tao_monitor -tao_ls_type armijo -tao_fmin 1e-6
./shepplogan -tao_monitor
```

## Brief Introduction to Optimization

Optimization algorithms seek to find the input variables or parameters (referred to as "control", 
"design" or "optimization" variables) that minimize (or maximize) a function of interest.

$$
\underset{p}{\text{minimize}} \quad f(p),
$$

where $$p \in \mathbb{R}^n$$ are the optimization variables and $$f(p): \mathbb{R}^{n} \rightarrow \mathbb{R}$$ is the 
objective function. In this lesson, we focus on gradient-based optimization methods -- methods that utilize information 
about the sensitivity of the objective function with respect to its inputs. 

Solutions to this problem are found where the gradient of the objective function is zero, $$\nabla_p f(p) = 0$$. 
However, this is only a *necessary* but not sufficient condition for optimality given that other stationary points 
(e.g. maxima) also satisfy this condition.

## Sequential Quadratic Programming

To find local minima for the above problems, we replace the original problem with a sequence of quadratic subproblems,

$$
\underset{d}{\text{minimize}} \quad f_k + d^Tg_k + \frac{1}{2}d^TH_kd^T,
$$

where $$g_k = \nabla_p f(p_k)$$ is the gradient, $$H_k = \nabla_p^2 f(p_k)$$ is the Hessian, $$d \in \mathbb{R}^n$$ is 
the search direction, and the $$k$$ subscript denotes evaluation at the iterate $$p_k$$. The exact solution to this 
quadratic subproblem is the inversion of the Hessian onto the negative gradient, $$d = -H_k^{-1} g_k$$. This can also be viewed as the application of the Newton root-finding method to the system of nonlinear equations defined by the optimality condition $$\nabla_p f(p) = 0$$.

In order to avoid non-minimum stationary points, we also seek to find a step length $$\alpha$$ that approximately 
minimizes the objective function along the line defined by the search direction,

$$
\underset{\alpha}{\text{minimize}} \Phi(\alpha) = f(p_k + \alpha d).
$$

This scalar minimization problem is called a "line search", and is categorized as a "globalization" method because it helps 
maintain consistency between the local quadratic model and the global nonlinear function.

The SQP class of algorithms can be summarized with the pseudocode:

![](sqp_pseudo.png){:width="25%"}

In this approach, different approximations to the search direction solution yield different members of the SQP family:

+ **Truncated Newton:** $$d = -H_k^{-1} g_k$$ with Hessian inverted iteratively (e.g. Krylov methods) using dynamic tolerances
+ **Quasi-Newton:** $$d = -B_k g_k$$ where $$B_k \approx H_k^{-1}$ with low-rank updates based on the Secant condition
+ **Conjugate Gradient:** $$d_k = -g_k + \beta d_{k-1}$$ with $$\beta$$ defining different CG update formulas
+ **Gradient Descent:** $$d = g_k$$ with Hessian replaced with the identity matrix

Further variations exist in combination with other globalization methods such as trust region and filter methods. In 
the present lecture, however, we only consider line search versions.

### PDE-constrained Optimization

Oftentimes we are interested in solving optimization problems where the evaluation of the objective function depends on 
the solution of a partial-differential-equation (PDE). These problems are represented in the most general case by

$$
\underset{p, u}{\text{minimize}} \quad f(p, u) \quad \text{subject to} \quad R(p, u) = 0,
$$

where $$u \in \mathbb{R}^m$$ are the state or solution variables for the PDE and 
$$R: \mathbb{R}^{n+m} \rightarrow \mathbb{R}^m$$ are the state equations (e.g. discretized PDE residual).

A common and convenient way to recast this problem is to represent the state variables as implicit functions of the 
optimization variables,

$$
\underset{p}{\text{minimize}} \quad f(p, u(p)).
$$

This eliminates the PDE constraint, converting the problem to an unconstrained version that can be solved by many 
popular unconstrained optimization algorithms. This comes at the cost of performing a complete PDE solution for every 
evaluation of the objective function, as well as an adjoint solution to efficiently compute gradients.

For more detail on PDE-constrained optimization, please refer to the ["Boundary Control with PETSc/TAO and AMReX" 
lecture from ATPESC 2019](https://xsdk-project.github.io/MathPackagesTraining/lessons/boundary_control_tao/).

## Using TAO

Toolkit for Advanced Optimization (TAO) is a package of optimization algorithms and tools developed at Argonne National 
Laboratory and distributed with the [Portable Extensible Toolkit for Scientific Computing (PETSc)][4] library. It is 
primarily intended for continuous gradient-based optimization, and supports PDE-constrained problems using the 
reduced-space formulation.

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
  ierr = VecCreateMPI(PETSC_COMM_WORLD, user.n, user.N,  &X);CHKERRQ(ierr);
  ierr = VecSet(X, 0.0);CHKERRQ(ierr);

  ierr = TaoCreate(PETSC_COMM_WORLD, &tao);CHKERRQ(ierr);
  ierr = TaoSetType(tao, TAOBQNLS);CHKERRQ(ierr); // TAOBQNLS Algorithm: Bounded Quasi-Newton Line Search
  ierr = TaoSetInitialVector(tao, X);CHKERRQ(ierr);
  ierr = TaoSetObjectiveAndGradientRoutine(tao, FormFunctionGradient, (void*) &user);CHKERRQ(ierr);
  ierr = TaoSetFromOptions(tao);CHKERRQ(ierr);
  ierr = TaoSolve(tao);CHKERRQ(ierr);

  ierr = VecDestroy(&X);CHKERRQ(ierr);
  ierr = TaoDestroy(&tao);CHKERRQ(ierr);
  ierr = PetscFinalize();
```

TAO calls the user-provided ``FormFunctionGradient()`` routine whenever the optimization algorithm needs to evaluate 
the objective and its gradient. The ``AppCtx`` structure contains any data the user has to preserve and propagate 
through for these computations.

## Example Problem: Multidimensional Rosenbrock

The Rosenbrock function is a canonical nonconvex test problem created by Howard H. Rosenbrock in 1960 and used 
extensively to evaluate the performance of optimization algorithms. The original function is given as 

$$
f(x_1, x_2) = (1 - x_1)^2 + 100(x_2 - x_1^2)^2
$$

with a global minimum at $$(1, 1)$$.

In this lecture, we will be using a multidimensional generalization of this problem given by

$$
f(x) = f(x_1, x_2, \dots, x_N) = \sum_{i=1}^{N-1} \left[ (1 - x_i)^2 + 100(x_{i+1} - x_i^2)^2 \right],
$$

for which the gradient is defined as

$$
\frac{df}{dx_1} = -400x_1(x_2 - x_1^2)^2 - 2(1-x_1)
$$

$$
\frac{df}{dx_j} = 200(x_j - x_{j-1}^2) - 400x_j(x_{j+1} - x_j^2) - 2(1 - x_j) \quad \forall j = 2, 3, \dots, N-1 
$$

$$
\frac{df}{dx_N} = 200(x_N - x_{N-1}^2)
$$



### Hands-on Activities

1. Change problem size with `-nx <size>` (default is 2) and evaluate its impact on performance. Now disable the 
analytical gradient and enable the finite difference gradient with `-fd`. Change problem size again and evaluate both 
convergence and iteration speed.

2. Run the problem in parallel using `mpiexec -np 4 ./multidim_rosenbrock...`. PETSc can seamlessly scale up 
the problem without changing the source code.

3. Change TAO algorithm to the nonlinear conjugate gradient method using `-tao_type bncg` or to truncated Newton using 
`-tao_type bnls`. Compare convergence with the default method (`bqnls` -- quasi-Newton line search). If necessary, 
change the convergence tolerances (using `-tao_fmin` and `-tao_gatol`) to help the problem converge.

## Example Problem: Shepp-Logan Phantom Image Reconstruction

Blah blah blah.

### Hands-on Activities

1. Solve the problem using different regularization terms.

2. Change the least-squares subsolver to a quasi-Newton method.

3. Try to manually construct the least-squares problem on your own and solve it using the Newton Line-Search (`bnls`) 
algorithm instead of letting BRGN construct the problem on its own. Evaluate if the solution is the same.

## Take-Away Messages

* Analytical derivatives are ideal for sensitivity analysis.
* When analytical derivatives are not available, PETSc/TAO can compute gradients automatically with finite differencing.
* PETSc/TAO offers parallel optimization algorithms for large-scale problems.
    - Optimization data is duplicated from user-generated PETSc vectors.
    - User has full control over parallel distribution and vector type.

## Further Reading

- [PETSc manual](https://www.mcs.anl.gov/petsc/petsc-current/docs/manual.pdf)  
- [TAO manual](https://www.mcs.anl.gov/petsc/petsc-current/docs/tao_manual.pdf)
- [PETSc/TAO website](https://www.mcs.anl.gov/petsc)

## Previous Optimization Lectures
- [ATPESC 2019](https://xsdk-project.github.io/MathPackagesTraining/lessons/boundary_control_tao/)
- [ATPESC 2018](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/lessons/obstacle_tao/)
