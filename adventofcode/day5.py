def load_input(filename: str) -> (list[list[str]], list[str]):
    with open(filename, "r") as f:
        data = [x.rstrip() for x in f.readlines()]

    s: list[str] = []
    commands: list[str] = []
    flag: bool = False
    for x in data:
        if x == "":
            flag = True
            continue
        if flag:
            commands.append(x)
        else:
            s.append(x)

    num_stacks: int = int(s[-1][-1])

    stacks: list[list[str]] = [[] for x in range(num_stacks + 1)]
    for i in range(len(s) - 2, -1, -1):
        for j in range(num_stacks):
            col: int = (1 + (j * 4))
            if col < len(s[i]) and s[i][col] != " ":
                stacks[j + 1].append(s[i][1 + (j * 4)])

    return stacks, commands


def solve_part1(s: list[list[str]], commands: list[str]) -> str:
    for cmd in commands:
        num: int = int(cmd.split()[1])
        f: int = int(cmd.split()[3])
        to: int = int(cmd.split()[5])

        for _ in range(num):
            crate: str = s[f].pop()
            s[to].append(crate)

    r: list[str] = []
    for i in range(1, len(s)):
        r.append(s[i][-1])

    return "".join(r)


def solve_part2(s: list[list[str]], commands: list[str]) -> str:
    for cmd in commands:
        num: int = int(cmd.split()[1])
        f: int = int(cmd.split()[3])
        to: int = int(cmd.split()[5])

        crates: list[str] = []
        for _ in range(num):
            crate: str = s[f].pop()
            crates.insert(0, crate)
        s[to] = s[to] + crates

    r: list[str] = []
    for i in range(1, len(s)):
        r.append(s[i][-1])

    return "".join(r)
