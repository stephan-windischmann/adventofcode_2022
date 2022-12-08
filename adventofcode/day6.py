def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


def solve_part1(data: str) -> int:
    for i in range(3, len(data)):
        if len(set(data[i - 4:i])) == 4:
            return i
    return -1


def solve_part2(data: str) -> int:
    for i in range(13, len(data)):
        if len(set(data[i - 14:i])) == 14:
            return i
    return -1
