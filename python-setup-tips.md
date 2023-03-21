# Python Setup Tips (Spring 2023)

## Dependency Management

Dependency management (i.e. keeping track of which packages are required for your project) is extremely important to ensure reusability and reproducibility of your code. 
To make this easier, you should create a new virtual environment for each project and use a tool to manage the dependencies of that environment.
We recommend using [poetry](https://python-poetry.org/) for this purpose (See more below).

## Python Versions and Python Interpreters

When working with Python, you might realize that there are multiple versions of Python installed on your system.
As a rule, you should never use the Python interpreter that comes preinstalled with your system.
Using it, and in particular installing packages with it, can lead to all kinds of problems with your operating system.

Further, when working with multiple projects, you will realize that you might need different versions of Python for different projects.

This means you should have a solid strategy for managing multiple Python versions and Python interpreters.

> **Note**
> In the past we recommended to use conda to manage Python versions.
> However, over the past years the default Python installation has improved significantly and you rarly run into issues with scientific packages anymore (which was the main reason to use conda in the past).
> Feel free to use conda if you prefer it, but the new way is more lightweight and easier to maintain in our opinion.

## Linux and MacOS

On Linux and MacOS, we recommend using [pyenv](https://github.com/pyenv/pyenv) to manage multiple Python versions.
You can install it using [Homebrew](https://brew.sh/) on MacOS or using your package manager on Linux.

Once you have installed pyenv, you can install the Python version you want to use for your project.
For example, to install Python 3.8.5, you can run:

```bash
pyenv install 3.8.5
```

If you use the cookiecutter templates, you can use the following command to find the path to the Python executable you just installed and then provide it for the `python_path` prompt (see [README.md](README.md)):

```bash
# For example for Python 3.8.5
echo $(pyenv shell 3.8.5; pyenv which python)
```

In case you have an existing project folder, you can set the local Python version to the one you just installed:

```bash
pyenv local 3.8.5
```

Note, this creates a new file called `.python-version` in your project folder.
You might want to add this file to your `.gitignore` file.

If you have configured the `virtualenvs.prefer-active-python` setting of poetry to `true`, poetry will automatically use the Python version you just installed.

If not, you can also tell poetry to use a specific Python version by running:

```bash
poetry env use $(pyenv shell 3.8.5; pyenv which python)
```

In both cases you might need to remove existing venvs of your project first and then run `poetry install` again.


## Windows

On Windows we recommend using the [py launcher](https://docs.python.org/3/using/windows.html#launcher) to manage multiple Python versions.
Simply install the Python versions you want using the official installer.
Then you can use the `py` command to select and switch between different Python versions.

For example, to install Python 3.8.5, you can run:

```powershell
py -3.8.5 -c "print('Hello World')"
```

If you use the cookiecutter templates, you can use the following command to find the path to the Python executable you just installed and then provide it for the `python_path` prompt (see [README.md](README.md)):

```powershell
# For example for Python 3.8.5
echo $(py -3.8.5 -c 'import sys; print(sys.executable)')
```

In case you have an existing project folder, you can tell poetry to use a specific Python version by running:

```powershell
poetry env use $(py -3.8.5 -c 'import sys; print(sys.executable)')```
```

You might need to remove existing venvs of your project first and then run `poetry install` again.

# Global Tooling

Some Python based tools are useful to have installed globally on your system and not duplicated in each project (or you want to have a global version in addition to a project specific version).

When these tools don't have a dedicated installer, and you just install them using `pip` in a single global Python environment, you might run into problems when these tools run into dependecy conflicts between themselves or with other tools you have installed globally.

Hence, we recommend using [pipx](https://pypa.github.io/pipx/) to install these tools.

## Poetry

We use poetry to manage our dependencies and to create our Python packages.
In addition, we use `poethepoet` (https://github.com/nat-n/poethepoet) as simple taskrunner withing projects.

> **Warning**
> Make sure you use poetry>=1.3 for everything we show below.

### Installation (using pipx)

This will install poetry (https://python-poetry.org) and the `poethepoet` command line tool globally on your system.
This allows you to use the `poetry` and the `poe` command everywhere on your system.

```
pipx install poetry
pipx inject poetry poethepoet --include-apps
```

Afterwards, you might want to enable tab completion for poetry and poethepoet:

1. https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh
2. https://github.com/nat-n/poethepoet#enable-tab-completion-for-your-shell

### Configuration

Poetry can be configured per project and globally.
Usually, you don't need to change much.
Only the `virtualenvs.in-project` setting is often modified.
If this is true, the virtual environment will be created in the `.venv` folder of your project.

This makes it easier to find (and delete) the virtual environment if you want to recreate it or if you need to do "surgery" on it.
However, if you are creating your project in a network drive, this can lead to problems with the virtual environment.
Decide for yourself what works best for you.

If you are using `pyenv` to manage your Python versions, you also might want to set the `virtualenvs.prefer-active-python` setting to `true`.
This allows poetry to automatically use the Python version you have set with `pyenv`.

## Jupyter Lab

Jupyter Lab is a great tool for interactive data analysis and visualization.
However, it is also quite "heavy" when it comes to install dependencies.
Hence, we only want to install it once on our system and not in each project.

### Installation (using pipx)

This installs jupyterlab and the `ipymp` extension globally on your system.
See more information about `ipympl` below.

```
pipx install jupyterlab --include-deps
pipx inject jupyterlab ipympl
```

In case you need to install more python based plugins (e.g. `jupytext`, `jupyter-bokeh`) use the `inject` command again.
For regular nodejs based plugins, you can use the `jupyter labextension install` command as usual.

To update jupyter and all injected dependencies, you can use the `upgrade` command:

```
pipx upgrade jupyterlab --include-injected
```

### Registering local kernels

Now that you have a global juptyerlab installation, you might need to register the kernels of your local projects.
For this, add `ipykernel` to your projects dev-dependencies and run the following command:

```
poetry run python -m ipykernel install --user --name <name-of-your-project>
```

If you are using the `ds-base` cookiecutter template, you can use the `poe` command to register a kernel pointing to the venv of your project:

```
poe conf_jupyter
```

In Jupyterlab, you can now select the kernel you just registered.

### The ipympl dilemma

The `ipympl` extension is a great tool to use matplotlib in Jupyterlab.
It allows you to zoom and pan in the plots created in your notebook (https://github.com/matplotlib/ipympl).

To make this possible, the extension has two components:
A Jupyterlab extension and a python package.
Because of our setup, Jupyterlab is running in a different Python environment than our kernels.
In result, the `ipympl` extension is not available in our kernels, and we need to add it to the dev-dependencies of our projects.

In this step we need to be extremely careful to pick the exact same version of the `ipympl` extension for Jupyterlab and for our kernels.
In case you run into problems (i.e. the plots are not showing), you should first figure our which version of `ipympl` is installed in your Jupyterlab environment and which is installed in your kernel environment.
Then you should make sure that both versions are the same.

For this, start the default kernel of your jupyterlab installation (usually called Python 3 (ipykernel)) and `import ipympl; print(ipympl.__version__)`.
Then repeat the same in the kernel of your project.

If the versions are different, we usually recommend to update the `ipympl` version in both environments to the latest one.
For your global installation run:
    
```
pipx upgrade jupyterlab --include-injected
```

and then in your local environment run:

```
poetry add ipympl@latest --group dev
```

Then restart jupyterlab and your kernel and check if the versions are now the same and if the plots are showing.

#### Maintaining multiple versions of ipympl

In case you can not easily update the version of ipympl in your project (e.g. because of reproducibility reasons), you can create a second global jupyterlab installation with a different version of ipympl.

```
# E.g. for ipympl 0.7
pipx install jupyterlab --include-deps --suffix "_ipympl_0_7"
pipx inject jupyterlab_ipympl_0_7 ipympl==0.7
```

Then you can launch this jupterlab version using the `jupyter_ipympl_0_7` command:
    
```
jupyter_ipympl_0_7 lab
```

## Global Python Environments

Sometimes you need global Python environments that are not bound to any projects.
We recommend using a "dummy" poetry project for this.
This allows you to use the same tooling as for your project specific environments.

Decide for yourself where you want to store these projects.
I put them into `~/.global_venvs`.

Hence, creating a new environment called `base` would look like this:

```
cd ~/.global_venvs
poetry new base
cd base
# Adapt this for windows/when using a different way of managing python versions
poetry env use $(pyenv shell 3.8.5; pyenv which python)  

poery add ipykernel --group dev  # If you need a kernel for jupyterlab
python -m ipykernel install --user --name base

poetry add numpy pandas matplotlib seaborn # Add your favorite packages
```

Then I can activate this python environment using the following command:

```
poetry -C ~/.global_venvs/base shell 
```

Or use the jupyterlab kernel registered above.


# IDE Integration

We recommend to use PyCharm (you can get the Pro-version, if you have an university email address) as your IDE in most cases.
For smaller Projects, you can also use VSCode.

Don't write large amounts of code in Jupyterlab!

For both VSCode and PyCharm, you need to specify the path to the python interpreter.
After running `poetry install`, use `poetry env info --path` to get the path to the python interpreter.
Then use this path in your IDE.
