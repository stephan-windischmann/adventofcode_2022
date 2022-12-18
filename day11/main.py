from adventofcode import day11


def solve_day11():
    monkeys: list[day11.Monkey] = day11.load_input("../input/day11/input")

    r1: int = day11.solve_part1(monkeys)
    print(f"Day 11 part 1 solution: {r1}")

    monkeys: list[day11.Monkey] = day11.load_input("../input/day11/input")

    r2: int = day11.solve_part2(monkeys)
    print(f"Day 11 part 2 solution: {r2}")


def main():
    solve_day11()


if __name__ == "__main__":
    main()
