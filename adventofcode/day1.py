def load_input(filename: str) -> list[list[int]]:
    cur: list[int] = []
    data: list[list[int]] = []

    with open(filename, "r") as f:
        for line in f.readlines():
            if line.strip() == "":
                data.append(cur)
                cur = []
            else:
                cur.append(int(line.strip()))

    data.append(cur)

    return data


def solve_part1(data: list[list[int]]) -> int:
    r: int = 0

    for elf in data:
        r = max(r, sum(elf))

    return r


def solve_part2(data: list[list[int]]) -> int:
    elf_calories = [sum(x) for x in data]
    elf_calories.sort(reverse=True)

    return sum(elf_calories[:3])
