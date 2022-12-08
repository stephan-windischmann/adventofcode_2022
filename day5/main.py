from adventofcode import day5


def solve_day5():
    s, commands = day5.load_input("../input/day5/input")

    r1: str = day5.solve_part1(s, commands)
    print(f"Day 5 part 1 solution: {r1}")

    s, commands = day5.load_input("../input/day5/input")

    r2: str = day5.solve_part2(s, commands)
    print(f"Day 5 part 2 solution: {r2}")


def main():
    solve_day5()


if __name__ == "__main__":
    main()
