import pandas as pd
from helpers import helper_functions as hf


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
    data["priority"] = data.apply(lambda row: ord(row.shared) - 38 if row.shared.isupper() else ord(row.shared) - 96, axis=1)

    return data.priority.sum()


def day_3_2(data):
    data.rename(columns={0: "pack"}, inplace=True)
    g = data.groupby(data.index // 3)
    groups = pd.DataFrame({
        "pack0": g.nth(0)["pack"],
        "pack1": g.nth(1)["pack"],
        "pack2": g.nth(2)["pack"]
    })
    groups["badge"] = groups.apply(lambda row: set(row.pack0).intersection(row.pack1, row.pack2).pop(), axis=1)
    groups["priority"] = groups.apply(lambda row: ord(row.badge) - 38 if row.badge.isupper() else ord(row.badge) - 96, axis=1)

    return groups.priority.sum()


def day_4_1(data):
    data.rename(columns={0: "elf_1_start", 1: "elf_1_end", 2: "elf_2_start", 3: "elf_2_end"}, inplace=True)
    return data.query('(elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end)').elf_1_start.count()


def day_4_2(data):
    data.rename(columns={0: "elf_1_start", 1: "elf_1_end", 2: "elf_2_start", 3: "elf_2_end"}, inplace=True)
    return data.query('(elf_1_start <= elf_2_start <= elf_1_end) or (elf_1_start <= elf_2_end <= elf_1_end) or (elf_2_start <= elf_1_start <= elf_2_end) or (elf_2_start <= elf_1_end <= elf_2_end)').elf_1_start.count()


def day_5_1(starting_state, instructions):
    boxes_state, instructions = day_5_prepare(starting_state, instructions)

    for instruction in instructions.iterrows():
        for i in range(instruction[1]['boxes_count']):
            boxes_state[instruction[1]['to_stack']].append(boxes_state[instruction[1]['from_stack']].pop())

    solution = ''
    for i in range(1, 10):
        solution += boxes_state[i].pop()
    return solution


def day_5_2(starting_state, instructions):
    boxes_state, instructions = day_5_prepare(starting_state, instructions)

    for instruction in instructions.iterrows():
        box_count = instruction[1]['boxes_count']
        boxes_state[instruction[1]['to_stack']].extend(boxes_state[instruction[1]['from_stack']][-box_count:])
        del boxes_state[instruction[1]['from_stack']][-box_count:]

    solution = ''
    for i in range(1, 10):
        solution += boxes_state[i].pop()
    return solution


def day_5_prepare(starting_state, instructions):
    boxes_state = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for line in reversed(starting_state):
        step = 1
        for box in line[1::4]:
            if box != ' ':
                boxes_state[step].append(box)
            step += 1

    instructions.drop(columns=[0, 2, 4], inplace=True)
    instructions.rename(columns={1: 'boxes_count', 3: 'from_stack', 5: 'to_stack'}, inplace=True)

    return boxes_state, instructions
