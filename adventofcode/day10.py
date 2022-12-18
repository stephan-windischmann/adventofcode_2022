def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def check_cycles(cycle: int, x: int, cycles: list[list[int]]):
    for c in cycles:
        if c[0] == cycle:
            c[1] = c[0] * x
            return


def solve_part1(commands: list[str]) -> int:
    cycles: list[list[int]] = [
        [20, 0],
        [60, 0],
        [100, 0],
        [140, 0],
        [180, 0],
        [220, 0],
    ]

    cycle: int = 1
    x: int = 1

    for cmd in commands:
        check_cycles(cycle, x, cycles)
        if cmd == "noop":
            cycle += 1
            continue
        add: int = int(cmd.split()[1])
        check_cycles(cycle + 1, x, cycles)
        cycle += 2
        x += add
    return sum([c[1] for c in cycles])


def draw_screen(cycle: int, x: int, screen: list[list[str]]):
    cur_x = cycle % 40
    cur_y = cycle // 40
    if x - 1 <= cur_x <= x + 1:
        screen[cur_y][cur_x] = "#"


def solve_part2(commands: list[str]) -> list[list[str]]:
    screen: list[list[str]] = []
    for _ in range(6):
        screen.append(["." for _ in range(40)])

    cycle: int = 0
    x: int = 1

    for cmd in commands:
        draw_screen(cycle, x, screen)
        if cmd == "noop":
            cycle += 1
            continue
        add: int = int(cmd.split()[1])
        draw_screen(cycle + 1, x, screen)
        cycle += 2
        x += add

    return screen
