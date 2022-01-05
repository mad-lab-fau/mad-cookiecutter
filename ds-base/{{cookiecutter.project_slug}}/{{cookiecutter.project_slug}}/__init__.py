# -*- coding: utf-8 -*-

__version__ = "{{cookiecutter.version}}"


def conf_rel_path():
    """Configure relative path imports for the experiments folder."""

    from pathlib import Path
    import sys

    parent_folder = str(Path("..").resolve())
    if parent_folder not in sys.path:
        sys.path.append(parent_folder)
