import os
import requests
from typing import Optional


def file_to_list(filename: str):
    if filename.startswith("http://") or filename.startswith("https://"):
        try:
            response = requests.get(filename)
            response.raise_for_status()  # Pastikan respons sukses
            return list(filter(bool, response.text.splitlines()))
        except requests.RequestException as e:
            raise FileNotFoundError(f"Error fetching URL {filename}: {e}")
    elif os.path.exists(filename):
        with open(filename, 'r+') as f:
            return list(filter(bool, f.read().splitlines()))
    else:
        raise FileNotFoundError(f"No such file or URL: '{filename}'")


def str_to_file(file_name: str, msg: str, mode: Optional[str] = "a"):
    with open(file_name, mode) as text_file:
        text_file.write(f"{msg}\n")


def shift_file(file):
    with open(file, 'r+') as f:  # open file in read / write mode
        first_line = f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
        return first_line.strip()
