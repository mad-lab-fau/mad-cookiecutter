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
    dev_deps = ["poethepoet", "pytest", "pytest-cov", "ruff"]
    doc_deps = ["numpydoc", "sphinx", "sphinx-gallery", "recommonmark", "memory-profiler", "matplotlib", "toml"]

    subprocess.run(["poetry", "add", "--lock", "--group", "dev", *dev_deps, *doc_deps])


def validate_project_slug():
    """Validate the project slug.

    We do that in the hook file to get the latest version for every new project.
    """
    project_slug = "{{ cookiecutter.project_slug }}"
    if not project_slug.isidentifier():
        raise ValueError(
            f"Project slug '{project_slug}' is not a valid Python identifier. "
            "A valid Python identifier is a non-empty string of letters, digits, and underscores."
        )


def configure_python_env():
    """Configure the Python environment for poetry."""
    python_path = "{{ cookiecutter.python_path }}"
    if python_path != "default":
        subprocess.run(["poetry", "env", "use", python_path])


if __name__ == "__main__":
    # Validate project slug
    validate_project_slug()
    # Configure Python environment
    configure_python_env()
    # Add custom configs
    configure_venv_folder()
    # Run Poetry check
    subprocess.run(["poetry", "check"])
    # Update all dependencies
    install_default_deps()
