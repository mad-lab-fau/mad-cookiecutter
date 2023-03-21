# MaD Cookiecutter Templates

A set of templates that can be used to quickly get started with a new project.

For all templates you need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/master):

```
pip install cookiecutter
```

Then follow the instructions for the template you want to use

## Datascience Project: `ds-base`

A base template for a typical datascience project.
This should be a good fit for a typical thesis project.

### Usage

First install:

- [poetry](https://python-poetry.org/docs/#installation)
- [poethepoet](https://github.com/nat-n/poethepoet) in your global python env (`pip install poethepoet`)

Then find the Python executable you want to use for your project.

When using pyenv, you can use:

```bash
# For example for Python 3.8
echo $(pyenv shell 3.8; pyenv which python)
```

On Windows 9using PowerShell and the `py` launcher:

```powershell
# For example for Python 3.8
echo $(py -3.8 -c 'import sys; print(sys.executable)')
```

When using conda, activate the environment of your base interpreter and run:

```bash
python -c 'import sys; print(sys.executable)'
```

Copy the full path for the next step!


Then run:

```bash
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="ds-base"
# Awnser all the prompts
# For python_path, use the path you copied in the previous step
cd my_project_name
git init
git commit -A -m'Initialised project based on mad-ds-base template'
poetry install
```

After creating a new project, check the README of your new project file.
It contains some basic information on how to get started.

### Features

- Dependency and venv management using `poetry`
- Installable core package for your algorithms
- Opinionated folder structure for data and experiments
- Automatic setup of formatting and lint tools (`black`, `ruff`)
- Support for either `nbstripout` or `jupytext` to handle notebooks in git
- Basic CI configuration for github and the mad-srv gitlab
- Commandline tools using `poethepoet`:
    - Helper to create boilerplate for individual experiments
    - Helper to manage project-specific jupyter kernels

## Python-Package: `py-package`

First install:

- [poetry](https://python-poetry.org/docs/#installation)
- [poethepoet](https://github.com/nat-n/poethepoet) in your global python env (`pip install poethepoet`)

Then find the Python executable you want to use for your project.

When using pyenv, you can use:

```bash
# For example for Python 3.8
echo $(pyenv shell 3.8; pyenv which python)
```

On Windows 9using PowerShell and the `py` launcher:

```powershell
# For example for Python 3.8
echo $(py -3.8 -c 'import sys; print(sys.executable)')
```

When using conda, activate the environment of your base interpreter and run:

```bash
python -c 'import sys; print(sys.executable)'
```

Copy the full path for the next step!


Then run:

```bash
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="py-package"
# Awnser all the prompts
# For python_path, use the path you copied in the previous step
cd my_project_name
git init
git commit -A -m'Initialised project based on mad-py-package template'
poetry install
```

Note, that you should specify a repo URL, even if you did not have a git repo yet.
At least specify `github.com` or `mad-srv.informatik.uni-erlangen.de` as this information is used to add specific configs.

### Features

- Dependency and venv management using `poetry`
- Automatic setup of formatting and lint tools (`black`, `ruff`)
- Basic docstructure and templates
- Basic CI configuration for github and the mad-srv gitlab


## Advanced Usage

For templates based on poetry, by default your main Python will be used.
To change which Python version should be used as basis for the new venv, use the `poetry env use /path/to/python` command.

