import pandas as pd
from helpers import helper_values as hv


def day_1_1(input_data):
    input_data = input_data.squeeze()
    elf_inventories = input_data.groupby(input_data.isna().cumsum()).sum()
    return int(elf_inventories.max())


def day_1_2(input_data):
    input_data = input_data.squeeze()
    elf_inventories = input_data.groupby(input_data.isna().cumsum()).sum()
    return int(elf_inventories.nlargest(3).sum())


def day_2_1(instructions):
    scores = instructions.replace({'A X': 4,
                                   'A Y': 8,
                                   'A Z': 3,
                                   'B X': 1,
                                   'B Y': 5,
                                   'B Z': 9,
                                   'C X': 7,
                                   'C Y': 2,
                                   'C Z': 6}
                                  )

    return scores.sum()[0]


def day_2_2(instructions):
    scores = instructions.replace({'A X': 3,
                                   'A Y': 4,
                                   'A Z': 8,
                                   'B X': 1,
                                   'B Y': 5,
                                   'B Z': 9,
                                   'C X': 2,
                                   'C Y': 6,
                                   'C Z': 7}
                                  )

    return scores.sum()[0]


def day_3_1(data):
    data.rename(columns={0: "pack"}, inplace=True)
    data["comp1"] = data.apply(lambda row: row.pack[:len(row.pack) // 2], axis=1)
    data["comp2"] = data.apply(lambda row: row.pack[len(row.pack) // 2:], axis=1)
    data["shared"] = data.apply(lambda row: set(row.comp1).intersection(set(row.comp2)).pop(), axis=1)
    data["priority_score"] = data["shared"].replace(hv.item_scores)

    return data["priority_score"].sum()


def day_3_2(data):
    g = data.groupby(data.index // 3)
    groups = pd.DataFrame({
        0: g.nth(0)[0],
        1: g.nth(1)[0],
        2: g.nth(2)[0]
    })

    groups['badge'] = groups.apply(lambda row: set(row[0]).intersection(set(row[1]), set(row[2])).pop(), axis=1)
    groups['badge_score'] = groups['badge'].replace(hv.item_scores)

    return groups['badge_score'].sum()
