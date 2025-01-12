#!/usr/bin/env python
from pathlib import Path
import subprocess
import re

def run_subprocess(command):
    """Run a subprocess command and raise an error if it fails."""
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout, stderr=result.stderr)
    return result


def install_default_deps():
    """Install some basic deps.

    We do that in the hook file to get the latest version for every new project.
    """

    ipympl_version = "{{cookiecutter.ipympl_version}}" if not "{{cookiecutter.ipympl_version}}" == "latest" else ""
    dev_deps = ["poethepoet", "pytest", "pytest-cov", "ipykernel", "ruff", f"ipympl{ipympl_version}"]

    if "{{cookiecutter.notebook_handling}}" == "nbstripout":
        dev_deps.append("nbstripout")
    elif "{{cookiecutter.notebook_handling}}" == "jupytext":
        dev_deps.append("jupytext")

    run_subprocess(["uv", "add", "--group", "dev", *dev_deps])



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
    
def validate_author():
    """Validate the author name."""
    author = "{{ cookiecutter.your_name }}"
    email = "{{ cookiecutter.email }}"
    if not author or not email:
        raise ValueError(
            "You must provide a valid author name and email address."
        )

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError(
            f"'{email}' is not a valid email address."
        )

def configure_python_env():
    """Configure the Python environment."""
    python_version = "{{ cookiecutter.used_python_version }}"
    run_subprocess(["uv", "python", "pin", python_version])


if __name__ == "__main__":
    # Validate project slug
    validate_project_slug()
    validate_author()
    # Configure Python environment
    configure_python_env()
    # Create data folder (We need to do that here, because the folder is ignored by git)
    Path("./data").mkdir()
    # Run Poetry check
    run_subprocess(["uv", "sync"])
    # Update all dependencies
    install_default_deps()
