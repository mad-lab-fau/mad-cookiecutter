#!/usr/bin/env python
import json
from pathlib import Path
import subprocess

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
    dev_deps = ["poethepoet", "pytest", "pytest-cov", "ruff"]
    doc_deps = ["numpydoc", "sphinx", "sphinx-gallery", "recommonmark", "memory-profiler", "matplotlib", "toml"]

    run_subprocess(["uv", "add", "--group", "dev", *dev_deps, *doc_deps])


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
    """Configure the Python environment."""
    python_version = "{{ cookiecutter.used_python_version }}"
    run_subprocess(["uv", "python", "pin", python_version])


if __name__ == "__main__":
    # Validate project slug
    validate_project_slug()
    # Configure Python environment
    configure_python_env()
    # Run uv check
    run_subprocess(["uv", "sync"])
    # Update all dependencies
    install_default_deps()
