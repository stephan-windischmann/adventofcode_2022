from adventofcode import day2


def solve_day2():
    data: list[str] = day2.load_input("../input/day2/input")

    r1: int = day2.solve_part1(data)
    print(f"Day 2 part 1 solution: {r1}")

    r2: int = day2.solve_part2(data)
    print(f"Day 2 part 2 solution: {r2}")


def main():
    solve_day2()


if __name__ == "__main__":
    main()
