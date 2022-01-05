# MaD Cookiecutter Templates

A set of templates that can be used to quickly get started with a new project.

## Getting started

First install:

- [cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/master): `pip install cookiecutter`
- [poetry](https://python-poetry.org/docs/#installation)
- [poethepoet](https://github.com/nat-n/poethepoet) in your global python env (`pip install poethepoet`)

```
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="ds-base"
```

_`ds-base` is the name of the specific template can be swapped out with a different subfolder name of this repo._

After creating a new project, check the README of your new project file.
It contains some basic information on how to get started.

If you have any questions or suggestions let us know in the issues!

## Advanced Usage

For templates based on poetry, by default your main Python will be used.
To change which Python version should be used as basis for the new venv, use the `poetry env use /path/to/python` command.

