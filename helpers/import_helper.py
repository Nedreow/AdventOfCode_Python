import pandas as pd


def import_into_pandas(year, filename, sep=" "):
    return pd.read_csv(
        "input_files/{}/{}.txt".format(year, filename),
        sep=sep,
        header=None,
        skip_blank_lines=False,
        engine='python'
    )


def import_as_string_series(year, filename):
    with open("input_files/{}/{}.txt".format(year, filename)) as instructions:
        lines = instructions.readlines()
    return lines


def import_as_string(year, filename):
    with open("input_files/{}/{}.txt".format(year, filename)) as f:
        data = f.read()
    return data
