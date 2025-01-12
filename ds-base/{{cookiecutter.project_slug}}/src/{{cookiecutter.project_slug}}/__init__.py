# -*- coding: utf-8 -*-


from pathlib import Path

# Do not change this line manually. It is automatically updated by bumpversion
__version__ = "{{cookiecutter.version}}" 

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def conf_rel_path():
    """Configure relative path imports for jupyter notebooks in the experiments folder."""

    import sys
    
    # This has to be `..`, because `__file__` does not work in Jupyter notebooks
    parent_folder = str(Path("..").resolve())
    if parent_folder not in sys.path:
        sys.path.append(parent_folder)