# AMReX -- a block-structured Adaptive Mesh Refinement (AMR) framework

## At a Glance
<!-- (Expected # minutes to complete) %% temporarily omit -->


```
Questions                 |Objectives                           |Key Points
--------------------------|----------- -------------------------|--------------------------
How do I start to use     | Understand easy set-up              | It's not hard to get started
AMReX?                    |                                     |
                          |                                     |
How do I 'turn on' AMR?   | Understand minimum specs for AMR    | When the algorithm is correctly designed
                          |                                     | and implemented, AMR 'just works'
                          |                                     |
How do I visualize AMR    | Use Visit for AMR results           | Visualization tools exist for AMR data.
results?
```
## Example: Multi-Level Advection

### The Equation and the Discretization

```
Mesh data only
AMR with subcycling
```

Let's consider scalar advection with a specified time-dependent velocity field.  In this example we'll be using AMR.

This algorithm may look familiar -- in each time step we construct fluxes and use them to update the solution.

Having the algorithm written in flux form allows straightforward "refluxing" at coarse-fine interfaces.

At each level:
```fortran
  ! Do a conservative update
  do    j = lo(2),hi(2)
     do i = lo(1),hi(1)
        phi_new(i,j) = phi_old(i,j) + &
             ( (flxx(i,j) - flxx(i+1,j)) * dtdx(1) &
             + (flxy(i,j) - flxy(i,j+1)) * dtdx(2) )
     enddo
  enddo
```

If "timeStep(lev,...)" advances the solution at level "lev" then
the subcycling in time algorithm looks like:
```C++
    if (lev < finest_level)
    {
        // recursive call for next-finer level
        for (int i = 1; i <= nsubsteps[lev+1]; ++i)
        {
            timeStep(lev+1, time+(i-1)*dt[lev+1], i);
        }

        if (do_reflux)
        {
            // update lev based on coarse-fine flux mismatch
            flux_reg[lev+1]->Reflux(*phi_new[lev], 1.0, 0, 0, phi_new[lev]->nComp(), geom[lev]);
        }

        AverageDownTo(lev); // average lev+1 down to lev
    }
```

### Running the Problem

Copy the directory AMReX_Advection from PATH_TO_AMREX_ADVECTION

In this directory you'll see

```
main2d.gnu.MPI.ex -- the executable
inputs_2d -- the inputs file
```

The inputs file currently has

```
max_step = 120
amr.n_cell = 64 64
amr.max_grid_size = 32
amr.plot_int = 10

```

The grid here is a cube consisting of 64 x 64 cells, consisting of 4 subgrids each
of size 32x32 cells.  The problem is periodic in the x-direction and not in the y-direction.
This problem happens to be set-up to have homogeneous Neumann boundary conditions when not periodic.

Let's try running this 2-d problem with no refinement

```
./main2d.gnu.MPI.ex inputs_2d amr.max_level=0
```

To see the 2-d solution, use Visit to look at plt00000 and plt00060, for example.
You should see something like this (though these pictures are
made using a different visualization program.)

|Time Step 0|Time Step 60|
|:---:|:---:|
|[<img src = "phi_adv_noref.0.jpg" width ="300">](phi_adv_noref.0.jpg)|[<img src = "phi_adv_noref.60.jpg" width ="300">](phi_adv_noref.60.jpg)

## Now let's turn on AMR.

Let's now run with
```
./main2d.gnu.MPI.ex inputs_2d amr.max_level=2
```

and again visualize the results.  

|Time Step 0|Time Step 60|
|:---:|:---:|
|[<img src = "phi_adv_ref.0.jpg" width ="300">](phi_adv_ref.0.jpg)|[<img src = "phi_adv_ref.60.jpg" width ="300">](phi_adv_ref.60.jpg)

## Example: "Off to the Races"

```
Cut cell / embedded boundary representation of obstacles
Linear solver
Particle advection in fluid flow
```

[Animation](macproj.gif)

The executable has been built already: main2d.gnu.MPI.ex

To run it in serial, 

```
./main2d.gnu.MPI.ex inputs
```

To run it in parallel, for example on 4 ranks:

```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs
```

The following parameters can be set at run-time -- these are currently set in the inputs
file but you can also set them on the command line.  

```
n_cell = 128                             # number of cells in x-direction; we double this in the y-direction
max_grid_size = 64                       # the maximum number of cells in any direction in a single grid

plot_int = 10                            # frequency of writing plotfiles

initial_tracer_file = tracers_file_2d    # name of file where we specify the input positions of the particles

time_step = 0.001                        # we advance the particles with a fixed time step of this size

max_time = 10.0                          # the final time (if max_time < max_steps * time_step)

max_steps = 10000                        # the maximum number of steps (if max_steps * time_step < max_time))

obstacles = 0 1 2 3 4 5 6 7 8            # this is how we choose which obstacles to include
```

The output from your run should look something like this:

```
********************************************************************
 You specified 9 objects in the domain: 0 1 2 3 4 5 6 7 8
 ********************************************************************

********************************************************************
 First let's project the initial velocity to find
   the flow field around the obstacles ...
********************************************************************


********************************************************************
 Done!  Now let's advect the particles ...
********************************************************************

Timestep 0, Time = 0.001 and leading particle now at 0.101179325
Timestep 100, Time = 0.101 and leading particle now at 0.2444506795
Timestep 200, Time = 0.201 and leading particle now at 0.4330191808
Timestep 300, Time = 0.301 and leading particle now at 0.5611955983
Timestep 400, Time = 0.401 and leading particle now at 0.7422046938
Timestep 500, Time = 0.501 and leading particle now at 0.8955689091
Timestep 600, Time = 0.601 and leading particle now at 1.044585496
Timestep 700, Time = 0.701 and leading particle now at 1.225885881
Timestep 800, Time = 0.801 and leading particle now at 1.34851225
Timestep 900, Time = 0.901 and leading particle now at 1.45538891
Timestep 1000, Time = 1.001 and leading particle now at 1.558181566
Timestep 1100, Time = 1.101 and leading particle now at 1.659474158
Timestep 1200, Time = 1.201 and leading particle now at 1.760129699
Timestep 1300, Time = 1.301 and leading particle now at 1.860489498
Timestep 1400, Time = 1.401 and leading particle now at 1.960718531

********************************************************************
We have a winner...and the winning time is 1.431
********************************************************************
```

## Example: AMReX-Pachinko

```
Cut cell / embedded boundary representation of obstacles
Particle-wall collisions
```
[Animation](pachinko.gif)

In this example we freeze the obstacles but can change the initial particle locations.

The executable has been built already: main2d.gnu.MPI.ex

To run it in serial, 

```
./main2d.gnu.MPI.ex inputs
```

To run it in parallel, for example on 4 ranks:

```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs
```

The following parameters can be set at run-time -- these are currently set in the inputs
file but you can also set them on the command line.  

```
n_cell = 125                             # number of cells in x-direction; we double this in the y-direction
max_grid_size = 25                       # the maximum number of cells in any direction in a single grid

plot_int = 10                            # frequency of writing plotfiles

initial_tracer_file = tracers_file_2d    # name of file where we specify the input positions of the particles

time_step = 0.001                        # we take a fixed time step of this size

max_time  = 3.0                          # the final time (if max_time < max_steps * time_step)
max_steps = 100000                       # the maximum number of steps (if max_steps * time_step < max_time))
```

For example, 
```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs initial_tracer_file=my_file
```

will read the particles from a file called "my_file"

The output from your run should look something like this:

```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs

********************************************************************
 Let's advect the particles ...
   We'll print a dot every 10 time steps.
********************************************************************

.............................................................................................................................................................................................................................................................................................................

********************************************************************
We've finished moving the particles to time 3
That took 1.145916707 seconds.
********************************************************************
```

### Follow-up Questions

{% include qanda question='Why might it be important to have n_cell be a power of 2 in the "Race" example
but not in the "Pachinko" example?' answer='In the "Race" example we use multigrid to solve for the flow field.'%}

### Further Reading

Download AMReX from github [here](https://www.github.com/AMReX-codes/amrex).

Look at the AMReX documentation/tutorials [here](https://amrex-codes.github.io/amrex/)

<!-- Insert space, horizontal line, and link to HandsOnLesson table -->

&nbsp;

---

[Back to all HandsOnLessons](../lessons.md)
