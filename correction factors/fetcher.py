import re
from pathlib import Path
from typing import List

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def get_files_path_list(path_to_directory: str) -> List[str]:
    directory = Path(path_to_directory)
    files_path_list = [str(file.absolute()) for file in directory.iterdir() if file.suffix == '.png']
    return files_path_list


def convert_to_number(string: str) -> float:
    mas_char = string.split()
    number = "".join(mas_char)
    number = float(number.replace(")", "").
                   replace("]", "").
                   replace(",", ".")
                   )

    return number


def get_statistical_data(mas_rows: List[str], file_path: str) -> List[float]:
    mas_stat = []
    for row in mas_rows:
        regex_num = re.compile('\d+')
        elem = regex_num.search(row)
        if elem:
            try:
                number = convert_to_number(row[elem.start():])
                mas_stat.append(number)
            except ValueError:
                print(f"bad input in file {file_path} ")
    return mas_stat


def get_data_from_file(file_path: str) -> list:
    data = pytesseract.image_to_string(file_path, lang='rus')
    mas_rows = data.split("\n")
    statistical_data = get_statistical_data(mas_rows, file_path)
    return statistical_data


def get_all_data(path_to_dir: str) -> List[List[float]]:
    stat_data_list = []
    files_path_to_img = get_files_path_list(path_to_dir)
    for file_path in files_path_to_img:
        stat_data = get_data_from_file(file_path)
        stat_data_list.append(stat_data)
    return stat_data_list


