---
layout: page-fullwidth
title: "AMReX"
subheadline: "A Block Structured Adaptive Mesh Refinement Framework"
teaser: "What can I do with AMReX..."
permalink: "lessons/amrex/"
use_math: true
lesson: true
header:
 image_fullwidth: "amrex_warpx2.png"
---

## At a Glance
<!-- (Expected # minutes to complete) %% temporarily omit -->

|Questions|Objectives|Key Points|
|What can I do with AMReX?|Understand that "AMR" means more<br>than just "traditional AMR"|AMR + EB + Particles|
|How do I get started?|Understand easy set-up|It's not hard to get started|
|How do I visualize AMR results|Use Visit for AMR results|Visualization tools exist for AMR data.|

## Example: Multi-Level Scalar Advection

### The Equation and the Discretization

|Capabilties|xxx|
|Mesh data|Dynamic AMR with subcycling|

$$\frac{\partial \phi}{\partial t} + \nabla \cdot (u \phi)  = 0$$

Let's consider scalar advection with a specified time-dependent velocity field.
In this example we'll be using AMR to resolve the scalar field.

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

The following parameters can be set at run-time -- these are currently set in the inputs
file but you can also set them on the command line.  

```
amr.max_time       =  2.0                # the final time (if max_time < max_steps * time_step)

amr.max_steps      = 1000000             # the maximum number of steps (if max_steps * time_step < max_time))

amr.n_cell         =  64   64   64       # number of cells at the coarsest AMR level in each coordinate direction

amr. max_grid_size = 32                  # the maximum number of cells in any direction in a single grid

amr.plot_int       = 10                  # frequency of writing plotfiles

adv.cfl            = 0.7                 # cfl number to be used for computing the time step

adv.phierr = 1.01  1.1  1.5              # regridding criteria  at each level

```

The base grid here is a cube consisting of 64 x 64 cells, consisting of 4 subgrids each
of size 32x32 cells.  The problem is periodic in both the x-direction and y-direction.


## Example: "Off to the Races"

```
+--------------------------+-------------------------------------+------------------------------------------+
| Capabilties              |                                     |                                          |
+--------------------------+-------------------------------------+------------------------------------------+
| Mesh data with EB        | Linear Solvers (Multigrid)          | Tracer Particles                         |
+--------------------------+-------------------------------------+------------------------------------------+
```

[Sample solution](macproj.gif)

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

For example, 
```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs obstacles = 1 3 4 5 6 8
```

will run the problem with only six obstacles -- see 

[Numbering](numbering.png)

to see the numbering scheme.


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
+--------------------------+--------------------------------------------------------------------------------+
| Capabilties              |                                                                                | 
+--------------------------+--------------------------------------------------------------------------------+
| EB for obstacles         | Particle-obstacle and particle-wall collisions                                 |
+--------------------------+-------------------------------------+------------------------------------------+
```

In this example particles accelerate downward with gravity and bounce off the side walls and off the solid obstacles.
There is no fluid but we still sort the particles according to our spatial decomposition of the domain.

This particular domain decomposition results from using a z-order space-filling curve with 
the number of cells per grid as the cost function.

[Sample domain decomposition](domain.png)

For now we freeze the obstacles (although if you look in the code it's not hard to figure out
how to change them!) but we can change the initial particle locations at run-time.

[Sample solution](pachinko.gif)

The executables have been built already: main2d.gnu.MPI.ex and main3d.gnu.MPI.ex

Note that in this specific example the problem is the same in both 2d and 3d since we assume the 
particles never move in the z-direction.

To run in serial, 

```
./main2d.gnu.MPI.ex inputs_2d
or
./main3d.gnu.MPI.ex inputs_3d
```

To run in parallel, for example on 4 ranks:

```
mpirun -n 4 ./main2d.gnu.MPI.ex inputs_2d
or
mpirun -n 4 ./main3d.gnu.MPI.ex inputs_3d
```

The following parameters can be set at run-time -- these are currently set in the inputs_2d
file but you can also set them on the command line.  In this specific example we use only 4
cells in the z-direction (if in 3-d) regardless of n_cell.

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
mpirun -n 4 ./main2d.gnu.MPI.ex inputs_2d initial_tracer_file=my_file
```

will read the particles from a file called "my_file"

The output from your run should look something like this:

```
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

To visualize the Pachinko results with yt, 
```
1) make sure you are using a bash shell
2) type "make movie"
3) visualize the animated gif "pachinko.gif"
```

To visualize the Pachinko results with paraview, follow the commands here:
[Paraview instructions](amrex-pachinko.pdf)

### Follow-up Questions

{% include qanda question='Why might it be important to have n_cell be a power of 2 in the "Race" example
but not in the "Pachinko" example?' answer='In the "Race" example we use multigrid to solve for the flow field.'%}

{% include qanda question='How do I build an AMReX-based code in 2D vs 3D?' answer='set DIM=2 vs DIM=3 in the GNUmakefile'%}

{% include qanda question='How do I build a serial version vs a parallel version of an AMReX-based code?'
answer='if you set USE_MPI=TRUE in the GNUmakefile then you can run in serial or parallel.'%}

{% include qanda question='How different is the Pachinko code itself for 2D vs 3D?'
answer='Not very!  Search for the test on AMREX_SPACEDIM in the source files to see how few lines are different.'%}

{% include qanda question='How could I make the parallel decomposition in the Pachinko example load balance
the particle work?' answer='Use a cost function based on number of particles instead of number of grid cells.'%}

### Suggested Evening Activities

1) In the "AMR 101" example, could I use what I learned in the SUNDIALS exercises to improve the accuracy 
   of the time-stepping?

2) In the "Off to the Races" example, what is the configuration of obstacles in which the 
   first particle reaches the end-line in the shortest time?

3) In the "Off to the Races" example, would a different linear solver be faster?   
   Try by setting USE_HYPRE = TRUE in the GNUmakefile (you'll need to re-make the executable)
   and add "use_hypre = 1"  to the command line

4) In the Pachinko example, how well can I control the final distribution of particles 
   from the initial particle positions?

### Further Reading

Download AMReX from github [here](https://www.github.com/AMReX-codes/amrex).

Look at the AMReX documentation/tutorials [here](https://amrex-codes.github.io/amrex/)

Read the Journal of Open Source Software (JOSS) paper [here](http://joss.theoj.org/papers/10.21105/joss.01370)

<!-- Insert space, horizontal line, and link to HandsOnLesson table -->

&nbsp;

---

[Back to all HandsOnLessons](../lessons.md)
