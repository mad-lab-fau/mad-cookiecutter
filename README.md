# MaD Cookiecutter Templates

A set of templates that can be used to quickly get started with a new project.

For all templates you need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/master) or use `pipx run cookiecutter`:

Then follow the instructions for the template you want to use.

> **Note:**
> We highly recommend reading our general [Python Setup Guide](https://github.com/mad-lab-fau/mad-cookiecutter/blob/main/python-setup-tips.md) before using any of the templates!

## Datascience Project: `ds-base`

A base template for a typical data science project.
This should be a good fit for a typical thesis or research paper project.

### Usage

First install:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [poethepoet](https://github.com/nat-n/poethepoet) by running `uv tool install poethepoet`

Then find the Python executable you want to use for your project.

When using pyenv, you can use:

```bash
# For example for Python 3.10
echo $(pyenv shell 3.10; pyenv which python)
```

On Windows using PowerShell and the `py` launcher:

```powershell
# For example for Python 3.10
echo $(py -3.10 -c 'import sys; print(sys.executable)')
```

When using conda, activate the environment of your base interpreter and run:

```bash
python -c 'import sys; print(sys.executable)'
```

Copy the full path for the next step!


Then run:

```bash
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="ds-base"
# Answer all the prompts
# For python_path, use the path you copied in the previous step
cd my_project_name
git init
git commit -A -m'Initialized project based on mad-ds-base template'
uv sync --dev
```

After creating a new project, check the README of your new project file.
It contains some basic information on how to get started.

### Features

- Dependency and venv management using [`uv`](https://docs.astral.sh/uv/)
- Installable core package for your algorithms
- Opinionated folder structure for data and experiments
- Automatic setup of formatting and lint tools ([`black`](https://github.com/psf/black), [`ruff`](https://docs.astral.sh/ruff/))
- Support for either [`nbstripout`](https://github.com/kynan/nbstripout) or [`jupytext`](https://jupytext.readthedocs.io/en/latest/) to handle notebooks in git
- Basic CI configuration for GitHub
- Commandline tools using [`poethepoet`]((https://github.com/nat-n/poethepoet)):
    - Helper to create boilerplate for individual experiments
    - Helper to manage project-specific jupyter kernels

## Python-Package: `py-package`

First install:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [poethepoet](https://github.com/nat-n/poethepoet) by running `uv tool install poethepoet`

Then find the Python executable you want to use for your project.

When using pyenv, you can use:

```bash
# For example for Python 3.10
echo $(pyenv shell 3.10; pyenv which python)
```

On Windows using PowerShell and the `py` launcher:

```powershell
# For example for Python 3.10
echo $(py -3.10 -c 'import sys; print(sys.executable)')
```

When using conda, activate the environment of your base interpreter and run:

```bash
python -c 'import sys; print(sys.executable)'
```

Copy the full path for the next step!


Then run:

```bash
cookiecutter gh:mad-lab-fau/mad-cookiecutter --directory="py-package"
# Answer all the prompts
# For python_path, use the path you copied in the previous step
cd my_project_name
git init
git commit -A -m'Initialized project based on mad-py-package template'
uv sync --dev
```

Note, that you should specify a repo URL, even if you did not have a git repo yet.
At least specify `github.com` or `mad-srv.informatik.uni-erlangen.de` as this information is used to add specific configs.

### Features

- Dependency and venv management using [`uv`](https://docs.astral.sh/uv/)
- Automatic setup of formatting and lint tools ([`black`](https://github.com/psf/black), [`ruff`](https://docs.astral.sh/ruff/))
- Basic doc structure and templates
- Basic CI configuration for GitHub


## Advanced Usage

### Using a different Python version

For templates based on `uv`, by default your main Python will be used.
To change which Python version should be used as basis for the new venv, use the `uv init -p <python-version>` command,
usually combined with `uv python pin <python-version>` to set the default Python version for the project and 
enforce the usage of the correct Python version in the venv.


### Publishing to PyPI and uploading code coverage to CodeCov

The `py-package` template is set up to provide GitHub actions to automatically publish your package to PyPI 
(on every release) and upload code coverage to CodeCov (on every push to main). For this to work, you need to
configure a few things:
1. **Publish to PyPI**: You need to enable Trusted Publisher for your package on PyPI. 
   This is a manual process and you need to follow the instructions on the
   [PyPI website](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) to add a new 
   pending publisher which will be converted to trusted publisher after the first release.
2. **CodeCov**: First, you need to create a CodeCov account (preferably by using your GitHub account).
   Then, you need to add the `CODECOV_TOKEN` secret to your GitHub repository by following the instructions on the
   [CodeCov website](https://docs.codecov.com/docs/adding-the-codecov-token).
   In order for the project to appear on CodeCov, you probably first need to initially push your code to GitHub.
   After adding the secret, the GitHub action will then automatically upload the code coverage to CodeCov on every 
   push to `main`.