import sys


def load_input(filename: str) -> set[tuple[int, int]]:
    m: set[tuple[int, int]] = set()

    with open(filename, "r") as f:
        for line in f.readlines():
            l: list[str] = line.split("->")
            coords = [(int(c.split(",")[0]), int(c.split(",")[1])) for c in l]
            for i in range(1, len(coords)):
                if coords[i - 1][0] == coords[i][0]:
                    x: int = coords[i][0]
                    for y in range(min(coords[i - 1][1], coords[i][1]),
                                   max(coords[i - 1][1], coords[i][1]) + 1):
                        m.add((x, y))
                else:
                    y: int = coords[i][1]
                    for x in range(min(coords[i - 1][0], coords[i][0]),
                                   max(coords[i - 1][0], coords[i][0]) + 1):
                        m.add((x, y))
    return m


def get_lowest_rock(m: set[tuple[int, int]]) -> int:
    lowest_rock: int = 0
    for coord in m:
        lowest_rock = max(lowest_rock, coord[1])

    return lowest_rock


def get_left_right_rocks(m: set[tuple[int, int]]) -> tuple[int, int]:
    left: int = sys.maxsize
    right: int = 0

    for coord in m:
        left = min(left, coord[0])
        right = max(right, coord[0])

    return left, right


def drop_sand(m: set[tuple[int, int]], start_point: tuple[int, int]) -> bool:
    lowest_rock: int = get_lowest_rock(m)

    if start_point[1] >= lowest_rock:
        return False

    if (start_point[0], start_point[1] + 1) in m:
        if (start_point[0] - 1, start_point[1] + 1) not in m:
            return drop_sand(m, (start_point[0] - 1, start_point[1] + 1))
        if (start_point[0] + 1, start_point[1] + 1) not in m:
            return drop_sand(m, (start_point[0] + 1, start_point[1] + 1))
        m.add(start_point)
        return True

    return drop_sand(m, (start_point[0], start_point[1] + 1))


def solve_part1(m: set[tuple[int, int]]) -> int:
    start_point = (500, 0)
    orig_len: int = len(m)

    while drop_sand(m, start_point):
        pass

    return len(m) - orig_len


def solve_part2(m: set[tuple[int, int]]) -> int:
    lowest_rock: int = get_lowest_rock(m)
    left_rock, right_rock = get_left_right_rocks(m)

    for y in range(lowest_rock + 2):
        for x in range(left_rock, right_rock + 1):
            if (x - 1, y - 1) in m and (x, y - 1) in m and (x + 1, y - 1) in m:
                m.add((x, y))

    sand_units: int = 0

    left: int = 500
    right: int = 500

    for y in range(lowest_rock + 2):
        for x in range(left, right + 1):
            if (x, y) not in m:
                sand_units += 1
        left -= 1
        right += 1

    return sand_units
