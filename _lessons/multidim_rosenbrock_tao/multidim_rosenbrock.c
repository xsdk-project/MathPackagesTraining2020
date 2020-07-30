#include <petsctao.h>
#include <mpi.h>
#include <time.h>

/* -------------------------------------------------------------------- */
/*
   User-defined application context - contains data needed by the
   application-provided call-back routines that evaluate the function,
   gradient, and hessian.
*/
typedef struct {
  PetscInt  n;             /* problem dimension */
  PetscMPIInt size, rank;  /* MPI process info */
} AppCtx;

/* ----------------------- Forward Declarations ----------------------- */
PetscErrorCode FormFunction(Tao,Vec,PetscReal*,void*);
PetscErrorCode FormGradient(Tao,Vec,Vec,void*);
PetscErrorCode FormHessian(Tao,Vec,Mat,Mat,void*);

/* -------------------------------------------------------------------- */
int main(int argc,char **argv)
{
  PetscErrorCode     ierr;                  /* used to check for function return/error codes */
  PetscReal          zero = 0.0;
  Vec                x;                     /* solution vector */
  Mat                H;                     /* Hessian matrix */
  Tao                tao;                   /* Tao solver context */
  PetscBool          flg, use_fd = PETSC_FALSE, sol_check = PETSC_TRUE;
  PetscReal          error, thresh = 1e-05;
  PetscInt           i, n;
  const PetscScalar *xx;
  double             start, end;
  AppCtx             user;                  /* user-defined application context */

  /* Initialize TAO and PETSc */
  ierr = PetscInitialize(&argc, &argv, (char*)0, (char*)0); if (ierr) return ierr;
  ierr = MPI_Comm_size(PETSC_COMM_WORLD, &user.size);CHKERRQ(ierr);
  ierr = MPI_Comm_rank(PETSC_COMM_WORLD, &user.rank);CHKERRQ(ierr);

  /* Initialize problem parameters */
  user.n = 2;

  /* Check for command line arguments to override defaults */
  ierr = PetscOptionsGetInt(NULL, NULL, "-n", &user.n, &flg);CHKERRQ(ierr);
  ierr = PetscOptionsGetBool(NULL, NULL, "-fd", &use_fd, &flg);CHKERRQ(ierr);

  /* Allocate vector for the solution */
  ierr = VecCreate(PETSC_COMM_WORLD, &x);CHKERRQ(ierr);
  ierr = VecSetSizes(x, PETSC_DECIDE, user.n);CHKERRQ(ierr);
  ierr = VecSetFromOptions(x);CHKERRQ(ierr);

  /* Allocate matrix for the Hessian */
  ierr = MatCreate(PETSC_COMM_WORLD, &H);CHKERRQ(ierr);
  ierr = MatSetSizes(H, PETSC_DECIDE, PETSC_DECIDE, user.n, user.n);CHKERRQ(ierr);
  ierr = MatSetFromOptions(H);CHKERRQ(ierr);
  ierr = MatSetUp(H);CHKERRQ(ierr);

  /* Create TAO solver with desired solution method */
  ierr = TaoCreate(PETSC_COMM_WORLD, &tao);CHKERRQ(ierr);
  ierr = TaoSetType(tao, TAOBQNLS);CHKERRQ(ierr);

  /* Set solution vec and an initial guess */
  ierr = VecSet(x, zero);CHKERRQ(ierr);
  ierr = TaoSetInitialVector(tao, x);CHKERRQ(ierr);

  /* Set routines for function, gradient, hessian evaluation */
  ierr = TaoSetObjectiveRoutine(tao, FormFunction, &user);CHKERRQ(ierr);
  if (use_fd) {
    ierr = TaoSetGradientRoutine(tao, TaoDefaultComputeGradient, &user);CHKERRQ(ierr);
    ierr = TaoSetHessianRoutine(tao, H, H, TaoDefaultComputeHessian, &user);CHKERRQ(ierr);
  } else {
    ierr = TaoSetGradientRoutine(tao, FormGradient, &user);CHKERRQ(ierr);
    ierr = TaoSetHessianRoutine(tao, H, H, FormHessian, &user);CHKERRQ(ierr);
  }

  /* Check for TAO command line options */
  ierr = TaoSetMaximumFunctionEvaluations(tao, 1000000);CHKERRQ(ierr);
  ierr = TaoSetMaximumIterations(tao, 1000);CHKERRQ(ierr);
  ierr = TaoSetTolerances(tao, 1e-05, 0.0, 0.0);CHKERRQ(ierr);
  ierr = TaoSetFromOptions(tao);CHKERRQ(ierr);

  /* Solve the problem */
  start = MPI_Wtime();
  ierr = TaoSolve(tao);CHKERRQ(ierr);
  end = MPI_Wtime();
  ierr = PetscPrintf(PETSC_COMM_WORLD, "\nTaoSolve() time: %f\n", end-start);CHKERRQ(ierr);

  /* Check solution */
  ierr = VecGetArrayRead(x, &xx);CHKERRQ(ierr);
  ierr = VecGetLocalSize(x, &n);CHKERRQ(ierr);
  for (i = 0; i < n; i++) {
    error = PetscAbs(xx[i] - 1.0);
    if (error > thresh) {
      sol_check = PETSC_FALSE;
      break;
    }
  }
  if (sol_check) {
    ierr = PetscPrintf(PETSC_COMM_WORLD, "\nSolution correct!\n");CHKERRQ(ierr);
  } else {
    ierr = PetscPrintf(PETSC_COMM_WORLD, "\nSolution wrong at index %i...\n", i);CHKERRQ(ierr);
  }
  
  /* Clean up PETSc objects */
  ierr = TaoDestroy(&tao);CHKERRQ(ierr);
  ierr = VecDestroy(&x);CHKERRQ(ierr);
  ierr = MatDestroy(&H);CHKERRQ(ierr);

  ierr = PetscFinalize();
  return ierr;
}

/* -------------------------------------------------------------------- */
/*
    FormFunction - Evaluates the objective function f(X).

    Input Parameters:
.   tao  - the Tao context
.   X    - input vector
.   ptr  - optional user-defined context, as set by TaoSetFunctionGradient()

    Output Parameters:
.   f - function value
*/
PetscErrorCode FormFunction(Tao tao,Vec X,PetscReal *f,void *ptr)
{
  AppCtx            *user = (AppCtx *) ptr;
  PetscInt          i;
  PetscErrorCode    ierr;
  PetscReal         ff=0,t1,t2;
  PetscReal         xghost;
  PetscInt          n;
  const PetscScalar *xx;

  PetscFunctionBeginUser;
  /* Get pointers to vector data */
  ierr = VecGetLocalSize(X, &n);CHKERRQ(ierr);
  ierr = VecGetArrayRead(X, &xx);CHKERRQ(ierr);

  /* Communicate boundary term to adjacent rank */
  if (user->rank != 0) {
    ierr = MPI_Send(&xx[0], 1, MPIU_REAL, user->rank-1, 123, PETSC_COMM_WORLD);CHKERRQ(ierr);
  }
  if (user->rank != user->size-1) {
    ierr = MPI_Recv(&xghost, 1, MPIU_REAL, user->rank+1, 123, PETSC_COMM_WORLD, MPI_STATUS_IGNORE);CHKERRQ(ierr);
  }

  /* Loop over local elements and add contribution to objective */
  ff = 0;
  for (i = 0; i < n-1; i++) {
    t1 = 1.0 - xx[i]; t2 = xx[i+1] - xx[i]*xx[i];
    ff += t1*t1 + 100.0*t2*t2;
  }

  /* Add contribution from element on adjacent rank */
  if ((user->size > 1) && (user->rank < user->size - 1)) {
    t1 = 1.0 - xx[n-1]; t2 = xghost - xx[n-1]*xx[n-1];
    ff += t1*t1 + 100.0*t2*t2;
  }

  /* Restore vectors */
  ierr = VecRestoreArrayRead(X, &xx);CHKERRQ(ierr);

  /* Sum local contributions to the global objective */
  ierr = MPI_Allreduce(&ff, f, 1, MPIU_REAL, MPIU_SUM, PETSC_COMM_WORLD);CHKERRQ(ierr);

  PetscFunctionReturn(0);
}

/* -------------------------------------------------------------------- */
/*
    FormGradient - Evaluates the gradient of the objective function G(X).

    Input Parameters:
.   tao  - the Tao context
.   X    - input vector
.   ptr  - optional user-defined context, as set by TaoSetFunctionGradient()

    Output Parameters:
.   G - vector containing the newly evaluated gradient
*/
PetscErrorCode FormGradient(Tao tao,Vec X,Vec G,void *ptr)
{
  AppCtx            *user = (AppCtx *) ptr;
  PetscInt          j;
  PetscErrorCode    ierr;
  PetscReal         xb, xa;
  PetscScalar       *gg;
  PetscInt          n;
  const PetscScalar *xx;

  PetscFunctionBeginUser;
  /* Get pointers to vector data */
  ierr = VecGetLocalSize(X, &n);CHKERRQ(ierr);
  ierr = VecGetArrayRead(X, &xx);CHKERRQ(ierr);
  ierr = VecGetArray(G, &gg);CHKERRQ(ierr);

  /* Communicate boundary terms to adjacent ranks */
  if (user->rank != 0) {
    ierr = MPI_Send(&xx[0], 1, MPIU_REAL, user->rank-1, 234, PETSC_COMM_WORLD);CHKERRQ(ierr);
    ierr = MPI_Recv(&xb, 1, MPIU_REAL, user->rank-1, 345, PETSC_COMM_WORLD, MPI_STATUS_IGNORE);CHKERRQ(ierr);
  }
  if (user->rank != user->size-1) {
    ierr = MPI_Send(&xx[n-1], 1, MPIU_REAL, user->rank+1, 345, PETSC_COMM_WORLD);CHKERRQ(ierr);
    ierr = MPI_Recv(&xa, 1, MPIU_REAL, user->rank+1, 234, PETSC_COMM_WORLD, MPI_STATUS_IGNORE);CHKERRQ(ierr);
  }

  /* First local element of the gradient */
  if (user->rank == 0) {
    gg[0] = -400.0*xx[0]*(xx[1] - xx[0]*xx[0]) - 2.0*(1.0 - xx[0]);
  } else {
    gg[0] = 200.0*(xx[0] - xb*xb) - 400.0*xx[0]*(xx[1] - xx[0]*xx[0]) - 2.0*(1.0 - xx[0]);
  }

  /* Interior elements */
  for (j = 1; j < n-1; j++) {
    gg[j] = 200.0*(xx[j] - xx[j-1]*xx[j-1]) - 400.0*xx[j]*(xx[j+1] - xx[j]*xx[j]) - 2.0*(1.0 - xx[j]);
  }

  /* Last local element of the gradient */
  if (user->rank == user->size-1) {
    gg[n-1] = 200.0*(xx[n-1] - xx[n-2]*xx[n-2]);
  } else {
    gg[n-1] = 200.0*(xx[n-1] - xx[n-2]*xx[n-2]) - 400.0*xx[n-1]*(xa - xx[n-1]*xx[n-1]) - 2.0*(1.0 - xx[n-1]);
  }

  /* Restore vectors */
  ierr = VecRestoreArrayRead(X, &xx);CHKERRQ(ierr);
  ierr = VecRestoreArray(G, &gg);CHKERRQ(ierr);

  PetscFunctionReturn(0);
}

/* ------------------------------------------------------------------- */
/*
   FormHessian - Evaluates Hessian matrix.

   Input Parameters:
.  tao   - the Tao context
.  x     - input vector
.  ptr   - optional user-defined context, as set by TaoSetHessian()

   Output Parameters:
.  H     - Hessian matrix

   Note:  Providing the Hessian may not be necessary.  Only some solvers
   require this matrix.
*/
PetscErrorCode FormHessian(Tao tao,Vec X,Mat H, Mat Hpre, void *ptr)
{
  AppCtx            *user = (AppCtx *) ptr;
  PetscInt          i;
  PetscErrorCode    ierr;
  PetscBool         assembled;
  PetscReal         xb, xa, vm, vd, vp;
  PetscInt          n, low, high, ind;
  const PetscScalar *xx;

  PetscFunctionBeginUser;
  /* Zero existing matrix entries */
  ierr = MatAssembled(H, &assembled);CHKERRQ(ierr);
  if (assembled){ierr = MatZeroEntries(H); CHKERRQ(ierr);}

  /* Get pointers to vector data */
  ierr = VecGetOwnershipRange(X, &low, &high);CHKERRQ(ierr);
  ierr = VecGetLocalSize(X, &n);CHKERRQ(ierr);
  ierr = VecGetArrayRead(X, &xx);CHKERRQ(ierr);

  /* Communicate boundary terms to adjacent ranks */
  if (user->rank != 0) {
    ierr = MPI_Send(&xx[0], 1, MPIU_REAL, user->rank-1, 234, PETSC_COMM_WORLD);CHKERRQ(ierr);
    ierr = MPI_Recv(&xb, 1, MPIU_REAL, user->rank-1, 345, PETSC_COMM_WORLD, MPI_STATUS_IGNORE);CHKERRQ(ierr);
  }
  if (user->rank != user->size-1) {
    ierr = MPI_Send(&xx[n-1], 1, MPIU_REAL, user->rank+1, 345, PETSC_COMM_WORLD);CHKERRQ(ierr);
    ierr = MPI_Recv(&xa, 1, MPIU_REAL, user->rank+1, 234, PETSC_COMM_WORLD, MPI_STATUS_IGNORE);CHKERRQ(ierr);
  }

  /* First local row */
  if (user->rank == 0) {
    vd = 1200.0*xx[0]*xx[0] - 400.0*xx[1] + 2.0;
    ierr = MatSetValue(H, 0, 0, vd, INSERT_VALUES);CHKERRQ(ierr);
    vp = -400.0*xx[0];
    ierr = MatSetValue(H, 0, 1, vp, INSERT_VALUES);CHKERRQ(ierr);
  } else {
    vm = -400.0*xb;
    ierr = MatSetValue(H, low, low-1, vm, INSERT_VALUES);CHKERRQ(ierr);
    vd = 202.0 + 1200.0*xx[0]*xx[0] - 400.0*xx[1];
    ierr = MatSetValue(H, low, low, vd, INSERT_VALUES);CHKERRQ(ierr);
    vp = -400.0*xx[0];
    ierr = MatSetValue(H, low, low+1, vp, INSERT_VALUES);CHKERRQ(ierr);
  }

  /* Loop over the interior of the Hessian */
  for (i = 1; i < n - 1; i++) {
    ind = low+i;
    vm = -400.0*xx[i-1];
    ierr = MatSetValue(H, ind, ind-1, vm, INSERT_VALUES);CHKERRQ(ierr);
    vd = 202.0 + 1200.0*xx[i]*xx[i] - 400.0*xx[i+1];
    ierr = MatSetValue(H, ind, ind, vd, INSERT_VALUES);CHKERRQ(ierr);
    vp = -400.0*xx[i];
    ierr = MatSetValue(H, ind, ind+1, vp, INSERT_VALUES);CHKERRQ(ierr);
  }

  /* Last local row */
  if (user->rank == user->size-1) {
    vm = -400.0*xx[n-2];
    ierr = MatSetValue(H, high-1, high-2, vm, INSERT_VALUES);CHKERRQ(ierr);
    vd = 200.0;
    ierr = MatSetValue(H, high-1, high-1, vd, INSERT_VALUES);CHKERRQ(ierr);
  } else {
    vm = -400.0*xx[n-2];
    ierr = MatSetValue(H, high-1, high-2, vm, INSERT_VALUES);CHKERRQ(ierr);
    vd = 202.0 + 1200.0*xx[n-1]*xx[n-1] - 400.0*xa;
    ierr = MatSetValue(H, high-1, high-1, vd, INSERT_VALUES);CHKERRQ(ierr);
    vp = -400.0*xx[n-1];
    ierr = MatSetValue(H, high-1, high, vp, INSERT_VALUES);CHKERRQ(ierr);
  }

  /* Restore vectors */
  ierr = VecRestoreArrayRead(X, &xx);CHKERRQ(ierr);

  /* Assemble matrix */
  ierr = MatAssemblyBegin(H, MAT_FINAL_ASSEMBLY);CHKERRQ(ierr);
  ierr = MatAssemblyEnd(H, MAT_FINAL_ASSEMBLY);CHKERRQ(ierr);

  PetscFunctionReturn(0);
}
