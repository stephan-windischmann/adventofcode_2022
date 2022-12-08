from adventofcode import day6


def solve_day6():
    data: str = day6.load_input("../input/day6/input")

    r1: int = day6.solve_part1(data)
    print(f"Day 6 part 1 solution: {r1}")

    r2: int = day6.solve_part2(data)
    print(f"Day 6 part 2 solution: {r2}")


def main():
    solve_day6()


if __name__ == "__main__":
    main()
