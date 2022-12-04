from adventofcode import day1


def solve_day1():
    data: list[list[int]] = day1.load_input("../input/day1/input")

    r1: int = day1.solve_part1(data)
    print(f"Day 1 part 1 solution: {r1}")

    r2: int = day1.solve_part2(data)
    print(f"Day 1 part 2 solution: {r2}")


def main():
    solve_day1()


if __name__ == "__main__":
    main()
