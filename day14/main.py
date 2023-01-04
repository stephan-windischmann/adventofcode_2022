from adventofcode import day14


def solve_day14():
    data = day14.load_input("../input/day14/input")

    r1: int = day14.solve_part1(data)
    print(f"Day 14 part 1 solution: {r1}")

    data = day14.load_input("../input/day14/input")

    r2: int = day14.solve_part2(data)
    print(f"Day 14 part 2 solution: {r2}")


def main():
    solve_day14()


if __name__ == "__main__":
    main()
