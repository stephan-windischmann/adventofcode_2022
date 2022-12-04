def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_part1(data: list[str]) -> int:
    overlapping: int = 0

    for pair in data:
        pairs = pair.split(",")
        a_min: int = int(pairs[0].split("-")[0])
        a_max: int = int(pairs[0].split("-")[1])
        b_min: int = int(pairs[1].split("-")[0])
        b_max: int = int(pairs[1].split("-")[1])
        if a_min <= b_min and b_max <= a_max or \
           b_min <= a_min and a_max <= b_max:
            overlapping += 1

    return overlapping


def solve_part2(data: list[str]) -> int:
    overlapping: int = 0

    for pair in data:
        pairs = pair.split(",")
        a_min: int = int(pairs[0].split("-")[0])
        a_max: int = int(pairs[0].split("-")[1])
        b_min: int = int(pairs[1].split("-")[0])
        b_max: int = int(pairs[1].split("-")[1])
        if a_min <= b_min <= a_max or \
           a_min <= b_max <= a_max or \
           b_min <= a_min <= b_max or \
           b_min <= a_max <= b_max:
            overlapping += 1

    return overlapping
