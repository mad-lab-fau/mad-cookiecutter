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
    dev_deps = ["black", "poethepoet", "pytest", "pytest-cov", "ruff"]
    doc_deps = ["numpydoc", "sphinx", "sphinx-gallery", "recommonmark", "memory-profiler", "matplotlib", "toml"]

    subprocess.run(["poetry", "add", "--lock", "--dev", *dev_deps, *doc_deps])


if __name__ == "__main__":
    # Add custom configs
    configure_venv_folder()
    # Run Poetry check
    subprocess.run(["poetry", "check"])
    # Update all dependencies
    install_default_deps()
