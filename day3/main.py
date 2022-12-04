from adventofcode import day3


def solve_day3():
    data: list[str] = day3.load_input("../input/day3/input")

    r1: int = day3.solve_part1(data)
    print(f"Day 3 part 1 solution: {r1}")

    r2: int = day3.solve_part2(data)
    print(f"Day 3 part 2 solution: {r2}")


def main():
    solve_day3()


if __name__ == "__main__":
    main()
