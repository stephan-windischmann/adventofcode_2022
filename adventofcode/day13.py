import ast
import math


def load_input(filename: str):
    data: list[str] = []
    with open(filename, "r") as f:
        data = f.readlines()

    r = []
    i: int = 0
    while i < len(data):
        r.append([ast.literal_eval(data[i]), ast.literal_eval(data[i + 1])])
        i += 3

    return r


def is_right_order(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    if isinstance(left, int) and isinstance(right, list):
        return is_right_order([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return is_right_order(left, [right])

    for i in range(min(len(left), len(right))):
        r = is_right_order(left[i], right[i])
        if r:
            return r
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


def solve_part1(data) -> int:
    r: int = 0

    for i, s in enumerate(data):
        if is_right_order(s[0], s[1]) <= 0:
            r += (i + 1)

    return r


def sort_all_messages(all_messages):
    swap: bool = True
    # Basic bubble sort.
    # Not very efficient but easy to implement :)
    while swap:
        swap = False
        for i in range(len(all_messages) - 1):
            if is_right_order(all_messages[i], all_messages[i + 1]) == 1:
                swap = True
                all_messages[i], all_messages[i + 1] = all_messages[i + 1], all_messages[i]


def solve_part2(data) -> int:
    dividers = [[[2]], [[6]]]
    all_messages = [x for x in dividers]

    for s in data:
        all_messages.append(s[0])
        all_messages.append(s[1])

    sort_all_messages(all_messages)

    dividers_index = []
    for i, s in enumerate(all_messages):
        if s in dividers:
            dividers_index.append(i + 1)

    return math.prod(dividers_index)
