class Monkey(object):
    def __init__(self, starting: list[int], operation: str, test: int, if_true: int, if_false: int):
        self.items = starting
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = 0

    def play_round(self, part1=True, scm=1) -> list[tuple[int, int]]:
        items: list[tuple[int, int]] = []

        while len(self.items) > 0:
            old = self.items.pop(0)
            new: int = eval(self.operation)
            if part1:
                new //= 3
            else:
                new %= scm
            if new % self.test == 0:
                items.append((new, self.if_true))
            else:
                items.append((new, self.if_false))
            self.inspect_count += 1

        return items


def load_input(filename: str) -> list[Monkey]:
    with open(filename, "r") as f:
        file = [x.strip() for x in f.readlines()]

    monkeys: list[Monkey] = []

    i: int = 0
    while i < len(file):
        items: list[int] = [int(x) for x in file[i + 1].split(":")[1].split(",")]
        operation: str = file[i + 2].split("=")[1].strip()
        test: int = int(file[i + 3].split()[-1])
        if_true: int = int(file[i + 4].split()[-1])
        if_false: int = int(file[i + 5].split()[-1])
        monkeys.append(Monkey(items, operation, test, if_true, if_false))
        i += 7

    return monkeys


def solve_part1(monkeys: list[Monkey]) -> int:
    num_rounds: int = 20

    for _ in range(num_rounds):
        for monkey in monkeys:
            for item in monkey.play_round():
                monkeys[item[1]].items.append(item[0])

    inspected_items: list[int] = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)

    return inspected_items[0] * inspected_items[1]


def solve_part2(monkeys: list[Monkey]) -> int:
    num_rounds: int = 10000

    tests: set[int] = set()
    for monkey in monkeys:
        tests.add(monkey.test)

    scm: int = 1
    for test in tests:
        scm *= test

    for _ in range(num_rounds):
        for monkey in monkeys:
            for item in monkey.play_round(part1=False, scm=scm):
                monkeys[item[1]].items.append(item[0])

    inspected_items: list[int] = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)

    return inspected_items[0] * inspected_items[1]
