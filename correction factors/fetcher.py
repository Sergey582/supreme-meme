from pathlib import Path
from typing import List


def get_files_path_list(path_to_directory: str) -> List[str]:
    directory = Path(path_to_directory)
    files_path_list = [str(file.absolute()) for file in directory.iterdir() if file.suffix == '.png']
    return files_path_list
