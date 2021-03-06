#!/usr/bin/env python
import json
from pathlib import Path
import subprocess


def configure_venv_folder():
    if "{{ cookiecutter.force_venv_in_folder }}" == "yes":
        subprocess.run(["poetry", "config", "virtualenvs.in-project", "true", "--local"])


def install_default_deps():
    """Install some basic deps.
    
    We do that in the hook file to get the latest version for every new project.
    """
    dev_deps = ["black", "poethepoet", "pytest", "pytest-cov", "prospector", "ipykernel"]

    if "{{cookiecutter.ipympl_version}}" == "latest":
        dev_deps.append("ipympl@latest")

    if "{{cookiecutter.notebook_handling}}" == "nbstripout":
        dev_deps.append("nbstripout")
    elif "{{cookiecutter.notebook_handling}}" == "jupytext":
        dev_deps.append("jupytext")

    subprocess.run(["poetry", "add", "--lock", "--dev", *dev_deps])


if __name__ == "__main__":
    # Create data folder (We need to do that here, because the folder is ignored by git)
    Path("./data").mkdir()
    # Add custom configs
    configure_venv_folder()
    # Run Poetry check
    subprocess.run(["poetry", "check"])
    # Update all dependencies
    install_default_deps()
