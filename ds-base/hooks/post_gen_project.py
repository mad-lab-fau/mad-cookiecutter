#!/usr/bin/env python
import json
from pathlib import Path
import subprocess



def configure_venv_folder():
    if "{{ cookiecutter.venv_in_folder }}" == "y":
        subprocess.run(["poetry", "config", "virtualenvs.in-project", "true", "--local"])

def install_default_deps():
    """Install some basic deps.
    
    We do that in the hook file to get the latest version for every new project.
    """
    if "{{cookiecutter.ipympl_version}}" == "latest":
        subprocess.run(["poetry", "add", "--dev", "ipympl@latest"])

    dev_deps =  ["black", "poethepoet", "pytest", "pytest-cov", "prospector", "ipykernel"]
    subprocess.run(["poetry", "add", "--dev", *dev_deps])



if __name__ == "__main__":
    # Add custom configs
    configure_venv_folder()
    # Update all dependencies
    install_default_deps()
    # Run Poetry check
    subprocess.run(["poetry", "check"])
