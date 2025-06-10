import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence

HERE = Path(__file__).parent


def task_new_experiment():
    if len(sys.argv) < 2:
        raise ValueError("Please provide the name of the new experiment as an argument.")
    name = sys.argv[1]
    files = ["__init__.py", "helper/__init__.py", "notebooks/.gitkeep", "scripts/.gitkeep", "README.md"]

    base_path: Path = HERE / "experiments" / name
    if base_path.is_file() or base_path.is_dir():
        raise ValueError(f"Experiment with name {name} already exists at {base_path}")

    for f in files:
        path = HERE / "experiments" / name / f
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch(exist_ok=True)

def update_version_strings(file_path, new_version):
    # taken from:
    # https://stackoverflow.com/questions/57108712/replace-updated-version-strings-in-files-via-python
    version_regex = re.compile(r"(^_*?version_*?\s*=\s*\")(\d+\.\d+\.\d+-?\S*)\"", re.M)
    with file_path.open("r+") as f:
        content = f.read()
        f.seek(0)
        f.write(
            re.sub(
                version_regex,
                lambda match: '{}{}"'.format(match.group(1), new_version),
                content,
            )
        )
        f.truncate()


def update_version(version: Sequence[str]):
    if len(version) == 0:
        # no argument passed => return the current version
        subprocess.run(["uv", "version"], shell=False, check=True, capture_output=False)
    else:
        # update the version
        subprocess.run(["uv", "version", *version], shell=False, check=True)
        new_version = (
            subprocess.run(["uv", "version"], shell=False, check=True, capture_output=True)
            .stdout.decode()
            .strip()
            .split(" ", 1)[1:][0]
        )

        update_version_strings(HERE.joinpath("src/{{cookiecutter.project_slug}}/__init__.py"), new_version)


def task_update_version():
    version_arr = sys.argv[1:] if len(sys.argv) > 1 else []
    update_version(version_arr)
