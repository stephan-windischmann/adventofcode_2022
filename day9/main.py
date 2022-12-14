from adventofcode import day9


def solve_day9():
    data: list[str] = day9.load_input("../input/day9/input")

    r1: int = day9.solve_part1(data)
    print(f"Day 9 part 1 solution: {r1}")

    r2: int = day9.solve_part2(data)
    print(f"Day 9 part 2 solution: {r2}")


def main():
    solve_day9()


if __name__ == "__main__":
    main()
