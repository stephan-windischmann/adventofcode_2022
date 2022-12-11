from adventofcode import day7


def solve_day7():
    commands: str = day7.load_input("../input/day7/input")

    r1: int = day7.solve_part1(commands)
    print(f"Day 7 part 1 solution: {r1}")

    r2: int = day7.solve_part2(commands)
    print(f"Day 7 part 1 solution: {r2}")


def main():
    solve_day7()


if __name__ == "__main__":
    main()
