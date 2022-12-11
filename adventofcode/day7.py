def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


class Directory:
    def __init__(self, name: str, parent: Directory):
        self.name: str = name
        self.subdirectories: list[Directory] = []
        self.parent: Directory = parent
        self.files: list[tuple[int, str]] = []

    def get_size(self):
        size: int = 0
        for f in self.files:
            size += f[0]

        for subdir in self.subdirectories:
            size += subdir.get_size()

        return size


def solve_part1(commands: list[str]) -> int:
    root_dir: Directory = Directory("/", None)
    cur_dir: Directory = root_dir
    all_dirs: list[Directory] = [root_dir]

    i: int = 1
    while i < len(commands):
        if commands[i].startswith("$"):
            if commands[i].split()[1] == "cd":
                dir_name: str = commands[i].split()[2]
                if dir_name == "..":
                    cur_dir = cur_dir.parent
                elif dir_name == "/":
                    cur_dir = root_dir
                else:
                    new_dir = Directory(dir_name, cur_dir)
                    cur_dir.subdirectories.append(new_dir)
                    cur_dir = new_dir
                    all_dirs.append(cur_dir)
                i += 1
            elif commands[i].split()[1] == "ls":
                i += 1
                while i < len(commands) and not commands[i].startswith("$"):
                    if not commands[i].split()[0] == "dir":
                        cur_dir.files.append((int(commands[i].split()[0]), commands[i].split()[1]))
                    i += 1

    size: int = 0

    for directory in all_dirs:
        dir_size: int = directory.get_size()
        if dir_size <= 100000:
            size += dir_size

    return size


def solve_part2(commands: list[str]) -> int:
    root_dir: Directory = Directory("/", None)
    cur_dir: Directory = root_dir
    all_dirs: list[Directory] = [root_dir]

    i: int = 1
    while i < len(commands):
        if commands[i].startswith("$"):
            if commands[i].split()[1] == "cd":
                dir_name: str = commands[i].split()[2]
                if dir_name == "..":
                    cur_dir = cur_dir.parent
                elif dir_name == "/":
                    cur_dir = root_dir
                else:
                    new_dir = Directory(dir_name, cur_dir)
                    cur_dir.subdirectories.append(new_dir)
                    cur_dir = new_dir
                    all_dirs.append(cur_dir)
                i += 1
            elif commands[i].split()[1] == "ls":
                i += 1
                while i < len(commands) and not commands[i].startswith("$"):
                    if not commands[i].split()[0] == "dir":
                        cur_dir.files.append((int(commands[i].split()[0]), commands[i].split()[1]))
                    i += 1

    root_dir_size: int = root_dir.get_size()
    remaining_space: int = 70000000 - root_dir_size

    min_to_delete: int = root_dir_size
    for directory in all_dirs:
        dir_size = directory.get_size()
        if remaining_space + dir_size >= 30000000:
            min_to_delete = min(min_to_delete, dir_size)

    return min_to_delete
