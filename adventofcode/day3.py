def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def get_priority(common: str) -> int:
    if ord(common) > ord("Z"):
        return ord(common) - ord("a") + 1
    return ord(common) - ord("A") + 27


def solve_part1(data: list[str]) -> int:
    priority: int = 0

    for line in data:
        common: str = \
            set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:])).pop()
        priority += get_priority(common)

    return priority


def solve_part2(data: list[str]) -> int:
    priority: int = 0

    for i in range(0, len(data), 3):
        common: str = set(data[i]).intersection(set(data[i + 1]), set(data[i + 2])).pop()
        priority += get_priority(common)

    return priority
