import datetime
import os
import platform
import re
import sys

# from globals import IDENTIFIER


# --------------------------------------------------------------------<FILE | PATH>-------------------------------------------------------------------- #
def regex_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def get_file_size(file_path):

    return os.path.getsize(file_path)


def repair_filename(filename):
    filename = filename.replace("[", "(")
    filename = filename.replace("]", ")")
    filename = filename.replace(":", "-")

    return filename


def resource_path(relative=''):
    root = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    return os.path.join(root, 'app', 'data', relative)


def get_file_path():

    return "not implemented yet"


def create_archive_directory():

    return "not implemented yet"


def split_to_url(input):
    input = input.split("/")
    url = input[0] + "//" + input[2]
    path = "/".join(input[3:])

    return url, path


# --------------------------------------------------------------------</FILE | PATH>-------------------------------------------------------------------- #


# ----------------------------------------------------------------------<TERMINAL>---------------------------------------------------------------------- #
def clear():
    if platform.system() == "WINDOWS_SYSTEM":
        os.system('cls')
    else:
        os.system('clear')

    return


# ----------------------------------------------------------------------<\TERMINAL>---------------------------------------------------------------------- #


# ------------------------------------------------------------------------<TIME>------------------------------------------------------------------------ #
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def mil_to_str(mil):
    minutes = int((mil / (1000 * 60)) % 60)
    seconds = str(int((mil / 1000) % 60))

    if len(seconds) == 1:
        seconds = f"0{seconds}"

    return f"{minutes}:{seconds[0:2]}"


def str_to_mil(time):
    time = time.split(":")
    minutes = int(time[0])
    seconds = int(time[1])

    return (minutes * 60 + seconds) * 1000


# ------------------------------------------------------------------------</TIME>------------------------------------------------------------------------ #


# ------------------------------------------------------------------------<PARSING>------------------------------------------------------------------------ #
# def parse_meta_data(data: str) -> dict:
#     meta_str = str(data)
#     meta_data = {}
#
#     if ";" or "\n" in meta_str:
#         items = meta_str.split(";").split("\n")
#         for item in items:
#             pair = item.split("$")
#             if len(pair) > 1:
#                 meta_data[str(pair[0])] = str(pair[1])
#
#     if meta_str is not None and meta_data == { }:
#         meta_data[IDENTIFIER] = meta_str
#
#     return meta_data


def reformat_meta_data(meta_data):
    data = []

    for key, value in meta_data.items():
        data.append(f"{key}: {value}")
