def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def move_tail(head_x: int, head_y: int, tail_x: int, tail_y: int) -> (int, int):
    if head_y == tail_y and abs(head_x - tail_x) == 2:
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
    elif head_x == tail_x and abs(head_y - tail_y) == 2:
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1
    elif abs(head_x - tail_x) == 2 or abs(head_y - tail_y) == 2:
        if head_x > tail_x and head_y > tail_y:
            tail_x += 1
            tail_y += 1
        elif head_x < tail_x and head_y < tail_y:
            tail_x -= 1
            tail_y -= 1
        elif head_x > tail_x and head_y < tail_y:
            tail_x += 1
            tail_y -= 1
        else:
            tail_x -= 1
            tail_y += 1

    return tail_x, tail_y


def solve_part1(data: list[str]) -> int:
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    tail_visited = set()

    for cmd in data:
        steps = int(cmd.split()[1])
        for _ in range(steps):
            if cmd[0] == "R":
                head_x += 1
            elif cmd[0] == "L":
                head_x -= 1
            elif cmd[0] == "U":
                head_y -= 1
            elif cmd[0] == "D":
                head_y += 1
            tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
            tail_visited.add((tail_x, tail_y))

    return len(tail_visited)


def solve_part2(data: list[str]) -> int:
    knots = [[0, 0] for _ in range(10)]

    tail_visited = set()

    for cmd in data:
        steps = int(cmd.split()[1])
        for _ in range(steps):
            if cmd[0] == "R":
                knots[0][0] += 1
            elif cmd[0] == "L":
                knots[0][0] -= 1
            elif cmd[0] == "U":
                knots[0][1] -= 1
            elif cmd[0] == "D":
                knots[0][1] += 1
            for i in range(9):
                knots[i + 1][0], knots[i + 1][1] = move_tail(knots[i][0], knots[i][1], knots[i + 1][0], knots[i + 1][1])
            tail_visited.add((knots[9][0], knots[9][1]))

    return len(tail_visited)
