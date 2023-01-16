import pandas as pd


def import_input(year, day, sep=" "):
    return pd.read_csv("input_files/{}/{}.txt".format(year, day), sep=sep, header=None, skip_blank_lines=False)

