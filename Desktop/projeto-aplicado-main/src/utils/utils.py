
import pandas as pd
from pathlib import Path
import os


def check_folder(folder_path: str) -> None:
    if not Path(folder_path).exists():
        os.makedirs(folder_path)


def correct_zeros(x) -> int | float:
    return 1 if pd.to_numeric(x) == 0 else x
