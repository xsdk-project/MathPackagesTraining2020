---
layout: page
show_meta: false
title: "Setup Instructions"
subheadline: "Instructions to complete prior to August 6th."
header:
   image_fullwidth: "atpesc-1024x2746.jpg"
permalink: "/setup_instructions/"
---

Instructions here are divided into _required_ and _optional_ steps.
We expect everyone to, minimally, complete all _required_ steps here.
The _optional_ steps are likely to improve your experience by simplifying
or improving performance of certain operations.

## Required Steps

Please complete the following _required_ steps prior to the beginning of the session
on Tuesday, August 6th.

1. Log Into Cooley
  * Use secure shell with compression, and trusted X forwarding enabled
```
ssh -l <username> -C -Y cooley.alcf.anl.gov
```
1. Copy Installed Software
* Once you are logged into Cooley, please execute the following instruction
to create a local, editable copy of numerical package software.
```
cd ~
rsync -a {{site.handson_install_root}}/{{site.handson_root}} .
```
  * **Note 1:** do not include a trailing slash, `/` in the path argument.
  * **Note 2:** You may be asked periodically throughout the day to re-execute
this command to update your local copy if we discover changes are necessary.
1. Confirm you can compile and run an example
  * As a test case, use an example from hypre to confirm you can compile
    and run an example
```
qsub -I -n 1 -t 5 -A ATPESC2019 -q debug
cd HandsOnLessons/hand_coded_heat
make mpi_test
mpicc mpi_test.c -o mpi_test
mpiexec -n 4 ./mpi_test
Size=4, Rank=0
Size=4, Rank=1
Size=4, Rank=2
Size=4, Rank=3
exit
```
  * The `qsub` command reserves a cooley node for interactive work for 5 minutes.
    You may have to wait a moment for the interactive prompt on the reserved node to return.
  * The above commands produce makefile and execution output. In particular
    the last `echo` command should produce a `0` response.
1. As soon after 9:30am, Tuesday , August 6th as possible, allocate an interactive node on
   cooley. The following command allocates a single Cooley node (`-n 1`) for 480 minutes
   (`-t 480`) using the ATPESC2019 allocation (`-A ATPESC2019`) and the queue reservation (`-q R.ATPESC2019_0806_1`):
```
qsub -I -n 1 -t 480 -A ATPESC2019 -q R.ATPESC2019_0806_1 
```
The command blocks until the node is ready.  Until the allocation expires (480 minutes in this example), all commands executed in the returned session will run on the allocated compute node; `mpiexec` can be used directly instead of going through `qsub`.
  * **Note 1:** The special `-q R.ATPESC2019_0806_1` will not be functional until 9:30 am, August 6th and will go away at 5:30pm that same day. Another queue, `-q R.ATPESC2019_0806_2` will be used for *evening* hands-on lessons from 6:30pm to 9:30pm.
  * **Note 2:** Please **DO NOT** run MPI jobs on the login nodes. Instead, run them on an allocated compute node.
  * **Note 3:** Be aware, however, that any running job will be terminated when your allocation expires.
  * **Note 4:** To enable X windows for visualization on the compute node, you can open a new terminal and login to the allocated compute node by doing `ssh -Y cc0xx` (`cc0xx` is your node id)

## Visualization Tool Setup

### Local Installations

Results from various applications we use today may involve visualization with
[VisIt][visit], [ParaView][paraview] or other visualization tools. By far, the simplest and
most reliable way to setup any of these tools is to create a local installation on your laptop
and then transfer data files from cooley to visualize them locally. In track 4, you will
have alread learned how to do this. Nonetheless, for your convenience links to instructions for
installing these tools locally are provided here...
* For [VisIt][visit], go [here](https://wci.llnl.gov/simulation/computer-codes/visit/executables) to
  find a suitable bundled executable installation for your system and then download and install it.
* For [ParaView][paraview], go [here](https://www.paraview.org/download/)  to
  find a suitable bundled executable installation for your system and then download and install it.

<!---
  Alternatively, you may use [Spack][spack] to install [GLVis][glvis] and MFEM as like so
```
git clone https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
spack install mfem glvis
```
-->

Once you have installed these tools, you can run them in client/server mode to connect to cooley
and visualize here data there or you may move data from cooley to your local machine and 
visualize it locally.  But, manually logging in to move data files each time you need to
can become combersome. You can use a single `scp` command to copy many files using either
file [globbing](https://en.wikipedia.org/wiki/Glob_(programming)) or the `-r` recursive
command-line option to copy whole directory trees as for example...
```
scp "cooley:/tmp/imag00*.png" .
```
or
```
scp -r cooley:/foo/bar/tree .
```

Beyond that, you may also want to have a look at...

* [Setting Up & Using SSH Multiplexing / Control master](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Multiplexing)
* [Using SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
* [Mounting Filesystems Over SSHFS](https://wiki.archlinux.org/index.php/SSHFS)

to simplify the process of manually moving data over many iterations of examples and tests.

### Using Local Installations in Client-Server Mode
A benefit from installing these tools locally is that once you have them installed locally, you
can also configure them to run _client-server_ where you run an instance locally but use that
instance to log into a remote resource, such as cooley, and visualize data there without having
to manually transfer it locally. To setup these tools for client-server operation...
* Follow [these instructions](https://www.alcf.anl.gov/user-guides/visit-cooley) to setup and run [VisIt][visit] client-server to Cooley.
* Follow [these instructions](https://www.alcf.anl.gov/user-guides/paraview-cooley) to setup and run [ParaView][paraview] client-server to Cooley.

### Using Remote Visualization Tools Through VNC
If you don't want to bother with installing anything locally or if you run into problems with
that and/or if you don't want to constantly move data between cooley and your local system or setup
passwordless ssh for that, a final option is to use [VNC][vnc]. Setting up a VNC connection involves
a complex set of steps including SSH tunneling and port forwarding. It is described in some detail
[here](https://www.alcf.anl.gov/user-guides/remote-visualization-cooley-using-vnc). However, we
have created a shell script for you to run to simplify this process.

But, a few challenges in using VNC on cooley are...
* It is likely to be useful to you only if you are on OSX or Linux or have Cygwin on Windows.
* You must have some vnc client installed on your local system
  * It is built into OSX
  * On linux, you will need either _vncviewer_ or _vinagre_
* Only the twm window manager is available
* Windows can be sized way too large for the VNC wrapper window in which they are placed
* Cutting and pasting between VNC windows and other windows may not work as expected.

With all those warnings and caveats aside, in addition, the setup script we provide
does take the following actions to your login setup on cooley...
* It adds some lines to your `~/.ssh/config` file (for SSH control master)
* It changes your `~/.vnc/xstartup`
If you do not wont these files changed...please do not run this script.

Here are the steps
1. Download the vnc setup script to a suitable directory on your local machine

[atpesc_cooley_vnc_setup.sh]({{ site.baseurl }}{% link pages/atpesc_cooley_vnc_setup.sh %})

1. Run the script [but first fix file permissions]
```
chmod 755 ./atpesc_cooley_vnc_setup.sh
./atpesc_cooley_vnc_setup.sh <cooley-username>
```
1. It will prompt you for your cooley login password. Enter it as you normally would.
1. You may observer output such as...
```
Password: 
Warning: No xauth data; using fake authentication data for X11 forwarding.
Warning: No xauth data; using fake authentication data for X11 forwarding.
```
1. It will then ask you for a temporary VNC password. Use 8 chars, upper
and lower case and at least one digit. Please do not use the password used
here in this example.
```
Create temporary VNC Password: Hello246
```
1. It will ask you to confirm your password
```
You have entered "Hello246", is this correct?
1) Yes
2) No
```
1. Enter `1` for Yes or `2` for no and a chance to re-entry a password.
1. It will then attempt to allocate (e.g. reserve a node on cooley). While
the node reservation request is processing, it will periodically print a
messaging indicating it is still waiting for the allocation...
```
Warning: No xauth data; using fake authentication data for X11 forwarding.
Checking for allocation completion
process_mux_new_session: tcgetattr: Operation not supported by device
Warning: No xauth data; using fake authentication data for X11 forwarding.
Checking for allocation completion
Checking for allocation completion
Checking for allocation completion
Checking for allocation completion
Checking for allocation completion
Got allocation at cc006
```
1. Note, it can take a few minutes before an allocation is created. When
the allocation is ready, it prints the node id. Above, that is `cc006`.
1. It then sets up a tunneling VNC connection to that node on port 22590.
```
Warning: No xauth data; using fake authentication data for X11 forwarding.
[1] 2479360
Warning: No xauth data; using fake authentication data for X11 forwarding.
Attempting to connect VNC to localhost:22590 - If this fails you can reattempt this manually
```
1. If all goes well, you will be prompted to enter your vnc password to
connect to the vnc instance just created. Enter the password you created
above (e.g. `Hello246` in this example). Then, you should see a VNC window
appear like so with an xterm running in it on the allocated node.
![VNC Window ::](/images/vnc_window.png)
1. From here, you can
```
soft add +visit
soft add +paraview
```
to add VisIt and ParaView to your environment.
1. **Finally, remember that part of the process of using VNC is to acquire
a reserved allocation on cooley. So, you should not then also reserve any
other cooley nodes apart from the one reserved with VNC through this script.**


[visit]: https://visit.llnl.gov
[glvis]: http://glvis.org
[paraview]: https://www.paraview.org
[vnc]: https://en.wikipedia.org/wiki/Virtual_Network_Computing
[spack]: https://spack.io

