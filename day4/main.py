from adventofcode import day4


def solve_day4():
    data: list[str] = day4.load_input("../input/day4/input")

    r1: int = day4.solve_part1(data)
    print(f"Day 4 part 1 solution: {r1}")

    r2: int = day4.solve_part2(data)
    print(f"Day 4 part 2 solution: {r2}")


def main():
    solve_day4()


if __name__ == "__main__":
    main()
