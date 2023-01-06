from adventofcode import day15


def solve_day15():
    data = day15.load_input("../input/day15/input")

    r1: int = day15.solve_part1(data)
    print(f"Day 15 part 1 solution: {r1}")

    r2: int = day15.solve_part2(data)
    print(f"Day 15 part 2 solution: {r2}")


def main():
    solve_day15()


if __name__ == "__main__":
    main()
