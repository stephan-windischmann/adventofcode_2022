from adventofcode import day8


def solve_day8():
    trees: list[list[int]] = day8.load_input("../input/day8/input")

    r1: int = day8.solve_part1(trees)
    print(f"Day 8 part 1 solution: {r1}")

    r2: int = day8.solve_part2(trees)
    print(f"Day 8 part 2 solution: {r2}")


def main():
    solve_day8()


if __name__ == "__main__":
    main()
