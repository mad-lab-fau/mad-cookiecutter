import sys
from pathlib import Path

HERE = Path(__file__).parent


def task_new_experiment():
    name = sys.argv[1]
    files = ["__init__.py", "helper/__init__.py", "notebooks/.gitkeep", "scripts/.gitkeep", "README.md"]

    base_path: Path = HERE / "experiments" / name
    if base_path.is_file() or base_path.is_dir():
        raise ValueError(f"Experiment with name {name} already exists at {base_path}")

    for f in files:
        path = HERE / "experiments" / name / f
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch(exist_ok=True)
