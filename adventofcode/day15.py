def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_row_excluded(sensors: dict[tuple[int, int], int], row: int) -> list[list[int]]:
    excluded: list[list[int]] = []
    for sensor in sensors:
        dist_to_row: int = abs(row - sensor[1])
        if dist_to_row > sensors[sensor]:
            continue
        horiz_part: int = sensors[sensor] - dist_to_row
        excluded.append([sensor[0] - horiz_part, sensor[0] + horiz_part])
    excluded.sort()

    merged: list[list[int]] = [excluded.pop(0)]
    while len(excluded) > 0:
        cur = excluded.pop(0)
        if cur[0] <= merged[-1][-1] + 1:
            merged[-1][1] = max(merged[-1][1], cur[1])
        else:
            merged.append(cur)

    return merged


def get_row_excluded_count(excluded: list[list[int]], beacons: set[tuple[int, int]], row: int) -> int:
    return sum([x[1] - x[0] + 1 for x in excluded]) - sum([1 for beacon in beacons if beacon[1] == row])


def solve_part1(data: list[str], row: int = 2000000) -> int:
    sensors: dict[tuple[int, int], int] = {}
    beacons: set[tuple[int, int]] = set()

    for line in data:
        sensor_x: int = int(line.split()[2].split("=")[1][:-1])
        sensor_y: int = int(line.split()[3].split("=")[1][:-1])
        beacon_x: int = int(line.split()[8].split("=")[1][:-1])
        beacon_y: int = int(line.split()[9].split("=")[1])

        sensors[(sensor_x, sensor_y)] = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
        beacons.add((beacon_x, beacon_y))

    excluded: list[list[int]] = get_row_excluded(sensors, row)
    return get_row_excluded_count(excluded, beacons, row)


def solve_part2(data: list[str], max_x: int = 4000000, max_y: int = 4000000) -> int:
    sensors: dict[tuple[int, int], int] = {}
    beacons: set[tuple[int, int]] = set()

    for line in data:
        sensor_x: int = int(line.split()[2].split("=")[1][:-1])
        sensor_y: int = int(line.split()[3].split("=")[1][:-1])
        beacon_x: int = int(line.split()[8].split("=")[1][:-1])
        beacon_y: int = int(line.split()[9].split("=")[1])

        sensors[(sensor_x, sensor_y)] = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
        beacons.add((beacon_x, beacon_y))

    for y in range(max_y):
        row: list[list[int]] = get_row_excluded(sensors, y + 1)
        if len(row) > 1:
            distress_x: int = row[0][1] + 1
            distress_y: int = y + 1
            return distress_x * 4000000 + distress_y

    return -1
