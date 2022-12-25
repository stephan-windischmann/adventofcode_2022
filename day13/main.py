from adventofcode import day13


def solve_day13():
    data = day13.load_input("../input/day13/input")

    r1: int = day13.solve_part1(data)
    print(f"Day 13 part 1 solution: {r1}")

    r2: int = day13.solve_part2(data)
    print(f"Day 13 part 2 solution: {r2}")


def main():
    solve_day13()


if __name__ == "__main__":
    main()
