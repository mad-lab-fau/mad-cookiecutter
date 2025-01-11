# Python Setup Tips (Spring 2025)

> **Note**
> This is an opinionated guide assuming basic knowledge of Python and the command line.
> Many recommendations also assume that you are planning to work with multiple large Python projects and might be overkill, for very simple Python setups.

This is the updated version of this guide for 2025!
A lot has changed since the last version.
If you are looking for the Spring 2023 version click [here](https://github.com/mad-lab-fau/mad-cookiecutter/blob/af5c389fbe9ead2e1039a62a9d1414620c9c86f3/python-setup-tips.md)

The big update: No more separate tools... Just [uv](https://docs.astral.sh/uv/) for everything!

Just follow the [one line installation instruction for your system](https://docs.astral.sh/uv/getting-started/installation/).
And that is it! Really!

Before we explain the details how to use it, we should quickly explain this decision to switch to `uv`:

## Why uv?

UV is a new tool for everything related to the Python development workflow.
It is developed by Astral (you know, the fine people that brought us [ruff](https://github.com/astral-sh/ruff), the super fast Python linter).
This is also the main reason, why I am confident that switching to uv is a good idea.
The Astral team has shown that they understand the needs of Python developers and that they can deliver high quality tools.

Beyond that uv offers several compelling advantages:

- **Python Installation Management**: `uv` simplifies Python installation. You no longer need to remember how you installed Python. Just specify the desired Python version, and `uv` will handle the installation correctly.
- **Flexible Dependency Management**: `uv` provides more escape hatches than poetry. You can override transient dependencies if you know they are incorrect.
- **Dedicated Documentation for PyTorch**: `uv` has a [dedicated documentation page](https://docs.astral.sh/uv/guides/integration/pytorch/) for installing PyTorch, addressing most common annoyances.
- **Unified Tool**: `uv` replaces multiple tools (poetry, pyenv, pipx) with a single tool, making it particularly convenient when setting up a new machine.
- **Standalone Executable**: `uv` is a standalone executable, making it easy to install and use. In particular on machines like the HPC, where you might not have the permissions to install new packages, this is a big advantage.
- **Speed**: `uv` is fast, enabling some wild use cases.


## Dependency Management

Dependency management (i.e. keeping track of which packages are required for your project) is extremely important to ensure reusability and reproducibility of your code. 
To make this easier, you should create a new virtual environment for each project and within this environment maintain a list of dependencies (speficining the minimal requirements) as well as a dependency lock-file (storing the exact versions of packages you used at any given point in time).

`uv` can handle all of this for you and can create, update, and sync your virtual environment, a `pyproject.toml` file (specifying your dependencies), and a `poetry.lock` file (specifying the exact versions of your dependencies).

Learn everything about using projects with `uv` in the [uv documentation](https://docs.astral.sh/uv/guides/projects/).

`uv` has also support for [specifying dependencies in a single script](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies), which can be extremly handy to distribute small scripts in the team.
The only thing you have to do is to install `uv` on the target machine and then call `uv run script.py` to execute the script, and it will handle the installation of Python and the dependencies for you.

This brings us to the next point:

## Python Versions and Python Interpreters

When working with Python, you might realize that there are multiple versions of Python installed on your system.
As a rule, you should never use the Python interpreter that comes preinstalled with your system.
Using it, and in particular installing packages with it, can lead to all kinds of problems with your operating system.

Further, when working with multiple projects, you will realize that you might need different versions of Python for different projects.

This means you should have a solid strategy for managing multiple Python versions and Python interpreters.

In the past we recommended two tools for this: `pyenv` and `conda`.
With `uv` the python version management is directly integrated with your project, which makes since much easier.

Basically all relevant commands provide a `--python/-p` flag, which allows you to specify the Python version you want to use.
`uv` will then install the specified Python version for you and just use it:

```
# For a new project:
uv init -p 3.9  # Results in Python requirements >=3.9

# Usually you also want to pin the Python version in your project:
uv python pin 3.9 # This enforces the usage of Python 3.9 duriong development

# To run a script with a specific Python version:
uv run -p 3.9 script.py
```

Learn more about managing Python versions with `uv` in the [uv documentation](https://docs.astral.sh/uv/concepts/python-versions/).

> **Note**
> `conda` might still be the right choice, when you are working with a lot of non-python dependencies (e.g. C++ libraries), which can be installed with `conda` as well.
> But, be aware, that `uv` will detect an active conda environment and all `uv` commands will be executed in this environment.
> This means, that uv will install packages into the conda environment and not into the virtual environment of your project.
>
> If you use conda, you might be interested in `pixi` (https://pixi.sh/latest/) which tries to be the `uv` of the conda ecosystem (it uses [`uv` under the hood](https://github.com/astral-sh/uv/issues/1572#issuecomment-1957318567) for all python dependencies).


## Which Python Version to Use?

When installing Python or starting a new project, it might be tempting to use the latest Python version.
However, in particular in the scientific community, it is often the case that packages are not yet compatible with the latest Python version at release, and it can take some time (sometimes years) until they are.
Hence, double check that the packages you want to use are compatible with the Python version you want to use.
At the time of writing (Spring 2025), we would recommend Python 3.11.

When developing a package that you expect others to use, use the oldest Python version you can easily support.
At the time of writing (Spring 2025), this is probably Python 3.9.
This way, users of your package don't need to upgrade their Python version to use your package.
However, make sure you test your package for all Python versions you support (ideally using some automated CI pipeline).

# Global Tooling

Some Python based tools are useful to have installed globally on your system and not duplicated in each project (or you want to have a global version in addition to a project specific version).

When these tools don't have a dedicated installer, and you just install them using `pip` in a single global Python environment, you might run into problems when these tools run into dependency conflicts between themselves or with other tools you have installed globally.

Surprise, surprise, `uv` can help you with this as well.
`uv` ships with a subcommand called `uv tool` that can be used to run (or install) global executables.

Because `uv` is fast, just running the command is often good enough:

```
uv tool run <executable> [args...]
# or
uvx <executable> [args...]
```

For example to run the small demo tool `cowsay`:

```
uvx cowsay -t "Hello World"
```

If you want to install a tool globally, you can use the `install` command:

```
uv tool install cowsay
```
Then you can run `cowsay` from anywhere on your system without the `uv tool run` prefix.
Learn more about using global tools with `uv` in the [uv documentation](https://docs.astral.sh/uv/concepts/tools/).

Note that `uv tool` is limited compared to `pipx` when it comes to dependency injection. Executables from dependencies cannot be exposed globally. For more complex scenarios, you might still prefer using `pipx`.


## Jupyter Lab

One of the tools that I like to have globally installed is Jupyter Lab.
As it is quite a complex tool with many dependencies, I don't want to install it in every project.

### Installation

This installs jupyterlab and the `ipympl` extension globally on your system.
See more information about `ipympl` below.

```
uv tool install --with ipympl --with jupyterlab jupyter-core
```

In case you need to install more python based plugins (e.g. `jupytext`, `jupyter-bokeh`) add additional `--with` flags.

```
uv tool install --with ipympl --with jupytext --with jupyter-bokeh --with jupyterlab jupyter-core
```

For regular nodejs based plugins, you can use the `jupyter labextension install` command as usual.

To update jupyter and all injected dependencies, you can use the `upgrade` command:

```
uv tool upgrade jupyter-core
```

You can now start Jupyterlab from anywhere on your system using the following command:

```
jupyter lab
```

Note, that `jupyter-lab` (with dash instead of space) will not work with this setup!

### Registering local kernels

Now that you have a global juptyerlab installation, you will need to register the venvs of your local projects as seperate kernels.
For this, add `ipykernel` to your projects dev-dependencies and run the following command:

```
uv add ipykernel --group dev
uv run python -m ipykernel install --user --name <name-of-your-project>
```

If you are using the `ds-base` cookiecutter template, you can use the `poe conf_jupyter` command to register a kernel pointing to the venv of your project.

In Jupyterlab, you can now select the kernel you just registered.

### The ipympl dilemma

The `ipympl` extension is a great tool to use matplotlib in Jupyterlab.
It allows you to zoom and pan in the plots created in your notebook (https://github.com/matplotlib/ipympl).

To make this possible, the extension has two components:
A Jupyterlab extension (running in the jupyterlab GUI) and a python package (running in the kernel).
Because in our setup, Jupyterlab is running in a different Python environment than our kernels.
In result, the `ipympl` extension is not available in our kernels, and we need to add it to the dev-dependencies of our projects.

In this step we need to be extremely careful to pick the exact same version of the `ipympl` extension for Jupyterlab and for our kernels.
In case you run into problems (i.e. the plots are not showing), you should first figure our which version of `ipympl` is installed in your Jupyterlab environment and which is installed in your kernel environment.
Then you should make sure that both versions are the same.

For this, start the default kernel of your jupyterlab installation (usually called `Python 3 (ipykernel)`) and then run `import ipympl; print(ipympl.__version__)` in a cell.
Then repeat the same in the kernel of your project.

If the versions are different, we usually recommend updating the `ipympl` version in both environments to the latest version.
For your global installation run:
    
```
uv tool upgrade jupyter-core
```

and then in your local environment run:

```
uv add ipympl@latest --group dev
```

Then restart jupyterlab and your kernel and check if the versions are now the same and if the plots are showing.
If not, you might run into a different issue.
Check the browsers javascript console for errors and head over to the [ipympl github page](https://github.com/matplotlib/ipympl) for more information.

#### Maintaining multiple versions of ipympl

In case you can not easily update the version of ipympl in your project (e.g. because of reproducibility reasons), we need a way to temporarlily switch the version of ipympl in our global installation.
Luckily, we can do this with a one time execution of jupyter lab with `uv tool run`:

```
uvx --from jupyterlab --with "ipympl==0.7.0" jupyter-lab
```

Note, that this will not install the new version of ipympl in your global installation or modify your global installation in any way.
This means, if you want other extensions to be available, you need to list them explicitly in the command.

You can use this technique to also create a custom jupyterlab execution command for every project, if it requires specific extensions or versions of extensions.

## Other global commands

Below some other global commands that might be useful.
Most of them, I use only occasionally.
So I don't install them, but just use `uvx` to run them.

ruff (auto code formatter):
    
```
uvx ruff format --line-length 100 <file>
```

Cookiecutter (project template generator):

```
uvx cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="ds-base"
```

## Global Python Environments

Sometimes you need global Python environments that are not bound to any projects.
With uv, you have two options to do this:

Like with uv tools, you can have a "single-use" environment, which is only used for a single command.
You can use this to either just open a python shell or to run a script.

```
uv run -p 3.9 --no-project --with numpy python
uv run -p 3.9 --no-project --with flask my_script.py
```

You can repeat the `--with` flag to add more packages to the environment.
The `--no-project` flag is important, because otherwise uv would try to discover a project in the current directory and use the environment of this project.
To make sure the command is executed in a clean environment, use the `--no-project` flag.

For more advanced "single-script" use-cases, uv also supports specifing the dependencies [in the script itself](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies).
This can be extremely powerful, if you just want to distribute a small script to your team, without the need to setup a full project.

However, we still recommend having at least one general purpose environment around that you can open and use for some quick testing and prototyping.
We recommend using a "dummy" uv project for this.
This allows you to use the same tooling as for your project specific environments.

Decide for yourself where you want to store these projects.
I put them into `~/.global_venvs`.

Hence, creating a new environment called `base` would look like this:

```
mkdir ~/.global_venvs
cd ~/.global_venvs
uv init -p 3.11 base
uv add ipykernel
# Register a kernel for that environment:
uv run ipykernel install --user --name base

# Add all the packages you always want to have:
uv add numpy scipy pandas matplotlib seaborn ipympl
```

Then you can run commands against this environment like this:

```
uv --directory ~/.global_venvs/base run python
```

Or use the jupyterlab kernel registered above.

I like to make it even easier for me to interact with the environment by creating a shell alias.
Put this into your `.bashrc` or `.zshrc` (or ask a friendly LLM to translate these commands to your OS and shell):

```sh
GLOBAL_VENVS="${HOME}/.global_venvs"
alias buv='uv --directory ${GLOBAL_VENVS}/base'
alias bpy='buv run python'
# Note: The next alias only works if ipykernel is installed in the venv
alias bipy='buv run ipython'
```

This allows to simply call `bpy` to open a python shell in your global environment or use `buv` to run more complex commands.
This way you can use and manage the entire environment without navigating to the directory.

Uv even allows to add a couple of dependencies to the environment just for a single command (aka, they will not be permanently added to the environment):
```
buv --with xls-writer python
```


# IDE Integration

We recommend to use PyCharm (you can get the Pro-version, if you have a university email address) as your IDE in most cases.
For smaller Projects, you can also use VSCode.

Don't write large amounts of code in Jupyterlab!

For both VSCode and PyCharm, you need to specify the path to the python interpreter.
With uv, the python interpreter is located in the `.venv` directory of your project.
In most cases this is automatically detected by the IDE.


# Notebook Debugging

One of the biggest pain-points of the Jupyter Lab/Notebook + IDE on the side development approach is that you can not easily debug into your library code when executing cells in Jupyter.
There are two approaches on how to gain some of this ability.
Both of them are only described for PyCharm, but similar things should work in other IDEs

## Connecting to a remote debugging process

WARNING: I could never get this method to work on Linux!

In PyCharm using `Run -> Attach to running process` you should be able to select a currently running ipython/jupyter kernel.
When executing code in the kernel (i.e. running code in your notebook in the browser), it will be traced by the PyCharm debugger.
You should now be able to set breakpoints in code that is imported by the notebook.

## Executing the Notebook in the IDE directly

Using PyCharms Jupyter integration, you can execute your notebook inside the IDE and debugging "just works".
However, if you followed the Jupyter setup in this guide, PyCharm will complain that "Jupyter is not installed".
To fix this, we will connect PyCharm to our external jupyter installation.

Under `Languages & Frameworks -> Jupyter -> Jupyter Servers` you can set up a `Configured Server`.
For this start `jupyter lab` in the commandline like you usually would and check the output.
In your CLI there should be a localhost-link (including an access token).
Copy this over into the PyCharm config.
PyCharm will now use your Jupyter installation to run Notebooks.
Just remember, that you need to start the server in the commandline first, before using notebooks in the IDE.

I personally use a workflow, where I use the browser based jupyter lab most of the time, but when I need complicated debugging, I just open the notebook in PyCharm.


# Working on the HPC (partially FAU specific)

`uv` works great on the HPC. You just need to decide if you want to use the predefined Python versions available via the HPC (or via loading modules), or if you want to let `uv` manage Python versions.

The first option is, how you would usually work on the HPC.
You load a Python module (which uses conda under the hood) and then create a venv with this Python version.
To ensure that `uv` uses this python, set your project config to only allow system python versions (see [here](https://docs.astral.sh/uv/reference/settings/#python-preference)).
Double check that the correct Python version was used once the venv is created.

Note, that the environment will only work, if you load the correct Python module before activating the venv.

This is the reason, why I prefer to let `uv` manage the Python versions.
For this you do the opposite and tell `uv` to only use "managed" Python versions (aka uv will download and install the Python version for you).

An issue that you might run into, is that some of the drives are mounted via NFS.
When the uv cache is stored on a different drive than the project, you might run into performance issues, and uv will give you some warnings.
This is not the end of the world, but if it annoys you, either move the cache and the project to the same drive.
The cache location can be adjusted via the `UV_CACHE_DIR` environment variable or the `--cache-dir` flag in all relevant uv commands.

Also note, that the uv cache can grow quite large over time.
So put it in a place where you have a large enough storage quota.