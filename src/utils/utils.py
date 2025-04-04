from pandas import to_numeric
from pathlib import Path
from os import makedirs


def check_folder(folder_path: str) -> None:
    if not Path(folder_path).exists():
        makedirs(folder_path)


def correct_zeros(x) -> int | float:
    return 1 if to_numeric(x) == 0 else x
