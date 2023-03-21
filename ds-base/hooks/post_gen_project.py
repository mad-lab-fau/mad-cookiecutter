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
    dev_deps = ["black", "poethepoet", "pytest", "pytest-cov", "ipykernel", "ruff"]

    if "{{cookiecutter.ipympl_version}}" == "latest":
        dev_deps.append("ipympl@latest")

    if "{{cookiecutter.notebook_handling}}" == "nbstripout":
        dev_deps.append("nbstripout")
    elif "{{cookiecutter.notebook_handling}}" == "jupytext":
        dev_deps.append("jupytext")

    subprocess.run(["poetry", "add", "--lock", "--group", "dev", *dev_deps])


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


if __name__ == "__main__":
    # Validate project slug
    validate_project_slug()
    # Create data folder (We need to do that here, because the folder is ignored by git)
    Path("./data").mkdir()
    # Add custom configs
    configure_venv_folder()
    # Run Poetry check
    subprocess.run(["poetry", "check"])
    # Update all dependencies
    install_default_deps()
