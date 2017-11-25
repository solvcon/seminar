<head><title>2017 SOLVCON Bootcamp</title></head>

# SOLVCON Bootcamp

In this event, participants will be guided to set up SOLVCON on Linux and run
the most basic example.  [Markdown version of this
page](https://github.com/solvcon/seminar/blob/gh-pages/2017/bootcamp/index.md)

* Where: TBD
* When: (tentative) 2017/12/8 15:30-18:30
* Instructor: [Yung-Yu Chen](mailto:yyc@solvcon.net), Taihsiang Ho
* [Sign-up sheet](https://github.com/solvcon/seminar/issues/7).  Please create
  a Github account (assuming you don't have one yet) and leave a message to
  sign up.

Last updated: 2017/11/25

## <a name="intro"></a> Introduction

SOLVCON needs a Unix-like system.  This bootcamp uses Ubuntu 14.04 Linux.
Afterwards you may also run it on mac osx on which SOLVCON is being actively
developed.

| Time          | Topic                             |
| :------------ | :-------------------------------- |
| 15:30 - 15:40 | [Overview & Introduction](#intro) |
| 15:40 - 16:00 | [SSH Remote Login](#ssh)          |
| 16:00 - 16:20 | [Git Basic](#git)                 |
| 16:20 - 16:30 | (No-coffee) break                 |
| 16:30 - 16:55 | [Install Anaconda](#conda)        |
| 16:55 - 17:20 | [Development Environment](#de)    |
| 17:20 - 17:30 | (No-coffee) break                 |
| 17:30 - 17:55 | [Build SOLVCON](#build)           |
| 17:55 - 18:20 | [Run a Case](#run)                |
| 18:20 - 18:30 | Q & A                             |

## <a name="ssh"></a> SSH Remote Login

A computational software package like SOLVCON usually needs powerful
workstations to crunch numbers.  Development and maintenance of SOLVCON require
similar environment.  We assume such an environment is ready and the first step
is to connect to the workstation.

We use a client-server architecture called "secure shell" (SSH).  The Linux
workstation has a SSH daemon configured and we may connect to it using a SSH
client.

* Windows: [https://www.chiark.greenend.org.uk/~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
* Linux and mac osx: system-provided "ssh" command.

ACTION: install or find the SSH client on your system, and try to run it
(although you may not have the information to connect at this point).

Instructor will provide you the following information:

1. Workstation host IP
2. Your user name
3. Your password

ACTION: use your SSH client to connect to the host.  Once successful, you may
see your username in the shell command prompt.

## <a name="git"></a> Set up User Environment: Git Basic

We practice basic usage of Git.  After you log into the account you have only
the basic environment setup.  Follow the steps to clone a Git repository and
use the files in it to set up your account.

ACTION: clone a repository to your home directory.

```bash
git clone https://github.com/yungyuc/workspace
```

ACTION: move the clone repository to home.

```bash
mv workspace/.git ~/
```

ACTION: check out the repository to update your home directory.

```bash
cd ~
git checkout -- .
```

ACTION: relogin.  You may see the shell prompt becomes different.

## <a name="conda"></a> Install Anaconda

SOLVCON depends on many third-party software packages.  Because SOLVCON needs
to support both Linux and mac osx, using the OS-provided package manager isn't
the most universal way to manage the dependency.  Thus SOLVCON chose Anaconda
for managing third-party packages.

The course server has downloaded an installer for you.  Execute the following
command to use it to install Anaconda:

```bash
bash /var/opt/conda3/packages/Miniconda3-latest-Linux-x86_64.sh
```

Note:

1. The installer asks for a destination path.  It's fine to keep the default.
2. We use the reduced version of Anaconda (called Miniconda).  It provides the
   same functionality with the full-version Anaconda, but the installer has
   fewer bundled packages.
3. You may relogin or run `source ~/.bashrc` to enable the installed Anaconda.

The course server also caches some packages.  After Anaconda is installed and
enabled, turn it on to save installation time:

```bash
conda config --system --add channels file:///var/opt/conda3/packages
```

## <a name="de"></a> Use Anaconda to Create Development Environment

Now we get the SOLVCON source repository.  In your home directory run the
following command:

```bash
git clone https://github.com/solvcon/solvcon
```

Git will clone the main SOLVCON repository to your `~/solvcon/`.  Change
working directory in it.

Anaconda supports creating independent runtime.  We use this feature to
segregate Python runtime for developing SOLVCON.  Run:

```bash
contrib/devenv/create.sh
```

It creates a conda environment in `build/env/`.  Now run `source
build/env/start` to enable the SOLVCON-specific conda environment.

## <a name="build"></a> Build SOLVCON and Run Tests

Before building SOLVCON we need to install the third-party packages it depends
on.  In the devenv, we install SOLVCON dependency using the following script:

```bash
contrib/conda.sh
```

Te above script uses `conda` and `pip` to install dependency.  Another
dependent package, pybind11, needs special treatment and there's a specific
script to install it:

```bash
contrib/build-pybind11-in-conda.sh
```

To this point we are ready to build SOLVCON.  Run:

```bash
python setup.py build_ext --inplace
```

After SOLVCON is built, run the unit tests:

```bash
nosetests --with-doctest
```

You may find a couple of errors regarding "boto".  It is caused by the course
server configuration.  It can be remedied by telling nose to ignore the server
configuration:

```bash
env BOTO_CONFIG=/tmp/nowhere nosetests --with-doctest
```

After the unit tests, also run a basic test for the gas-dynamic solver in
SOLVCON:

```bash
nosetests ftests/gasplus/*
```

At this point SOLVCON is built and tested with the regression tests.

You may see a terse version of the above description at [SOLVCON
README](https://github.com/solvcon/solvcon/blob/master/README.rst).

## <a name="run"></a> Run Shock Tube Problem

Enter the gas-dynamic functional test directory:

```bash
cd ftests/gasplus
```

And run the test case in the script mode:

```bash
python test_tube_2d_triangle_regular.py run tube_2d_triangle_regular_run
```

It produces a directory named `tube_2d_triangle_regular_run/`, which contains
the result VTK files.  Use [ParaView](https://www.paraview.org) to view them.
