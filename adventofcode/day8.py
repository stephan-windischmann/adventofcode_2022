def load_input(filename: str) -> list[list[int]]:
    trees: list[list[int]] = []
    with open(filename, "r") as f:
        for line in f.readlines():
            trees.append([int(x) for x in line.strip()])

    return trees


def solve_part1(trees: list[list[int]]) -> int:
    visited: list[list[bool]] = []

    visible: int = 0

    for x in trees:
        visited.append([False for _ in range(len(x))])

    for i in range(len(trees)):
        from_left: int = -1
        for j in range(len(trees[i])):
            if trees[i][j] > from_left:
                if not visited[i][j]:
                    visible += 1
                    visited[i][j] = True
                from_left = trees[i][j]

    for i in range(len(trees)):
        from_right: int = -1
        for j in range(len(trees[i]) - 1, -1, -1):
            if trees[i][j] > from_right:
                if not visited[i][j]:
                    visible += 1
                    visited[i][j] = True
                from_right = trees[i][j]

    for j in range(len(trees[0])):
        from_top: int = -1
        for i in range(len(trees)):
            if trees[i][j] > from_top:
                if not visited[i][j]:
                    visible += 1
                    visited[i][j] = True
                from_top = trees[i][j]

    for j in range(len(trees[0])):
        from_bottom: int = -1
        for i in range(len(trees) -1, -1, -1):
            if trees[i][j] > from_bottom:
                if not visited[i][j]:
                    visible += 1
                    visited[i][j] = True
                from_bottom = trees[i][j]

    return visible


def get_scenic_score(i: int, j: int, trees: list[list[int]]) -> int:
    left: int = 0
    right: int = 0
    up: int = 0
    down: int = 0

    for x in range(i + 1, len(trees), 1):
        down += 1
        if trees[x][j] >= trees[i][j]:
            break

    for x in range(i - 1, -1, -1):
        up += 1
        if trees[x][j] >= trees[i][j]:
            break

    for y in range(j + 1, len(trees[i]), 1):
        right += 1
        if trees[i][y] >= trees[i][j]:
            break

    for y in range(j - 1, -1, -1):
        left += 1
        if trees[i][y] >= trees[i][j]:
            break

    return left * right * up * down


def solve_part2(trees: list[list[int]]) -> int:
    top_scenic_score: int = 0

    for i in range(len(trees)):
        for j in range(len(trees[i])):
            top_scenic_score = max(top_scenic_score, get_scenic_score(i, j, trees))

    return top_scenic_score
