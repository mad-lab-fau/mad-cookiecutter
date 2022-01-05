# MaD Cookiecutter Templates

A set of templates that can be used to quickly get started with a new project.

For all templates you need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/master):

```
pip install cookiecutter
```

Then follow the instructions for the template you want ot use

## Datascience Project: `ds-base`

A base template for a typical datascience project.
This should be a good fit for a typical thesis project.

### Usage

First install:

- [poetry](https://python-poetry.org/docs/#installation)
- [poethepoet](https://github.com/nat-n/poethepoet) in your global python env (`pip install poethepoet`)

```
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="ds-base"
cd my_project_name
git init
git commit -A -m'Initialised project based on mad-ds-base template'
poetry install
```

After creating a new project, check the README of your new project file.
It contains some basic information on how to get started.

### Features

- Dependency and venv management using `poetry`
- Opinionated folder structure for data and experiments
- Automatic setup of formatting and lint tools (`black`, `isort`, `prospector`)
- Support for either `nbstripout` or `jupytext` to handle notebooks in git
- Commandline tools using `poethepoet`:
    - Helper to create boilerplate for individual experiments
    - Helper to manage project-specific jupyter kernels


## Advanced Usage

For templates based on poetry, by default your main Python will be used.
To change which Python version should be used as basis for the new venv, use the `poetry env use /path/to/python` command.

