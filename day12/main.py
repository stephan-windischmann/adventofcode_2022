from adventofcode import day12


def solve_day12():
    heightmap: list[list[str]] = day12.load_input("../input/day12/input")

    r1: int = day12.solve_part1(heightmap)
    print(f"Day 12 part 1 solution: {r1}")

    heightmap: list[list[str]] = day12.load_input("../input/day12/input")

    r2: int = day12.solve_part2(heightmap)
    print(f"Day 12 part 2 solution: {r2}")


def main():
    solve_day12()


if __name__ == "__main__":
    main()
