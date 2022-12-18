from adventofcode import day10


def solve_day10():
    commands: list[str] = day10.load_input("../input/day10/input")

    r1: int = day10.solve_part1(commands)
    print(f"Day 10 part 1 solution: {r1}")

    r2: list[list[str]] = day10.solve_part2(commands)
    print(f"Day 10 part 1 solution:")
    for line in r2:
        print("".join(line))


def main():
    solve_day10()


if __name__ == "__main__":
    main()
