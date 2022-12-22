import heapq
import sys


def load_input(filename: str) -> list[list[str]]:
    heightmap: list[list[str]] = []
    with open(filename, "r") as f:
        for line in f.readlines():
            heightmap.append(list(line.strip()))
    return heightmap


def shortest_distance(start: tuple[int, int], end: tuple[int, int], heightmap: list[list[str]]) -> int:
    q = []
    visited: set[tuple[int, int]] = set()
    heapq.heappush(q, (0, start))

    while len(q) > 0:
        cur_dist, cur_node = heapq.heappop(q)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        if cur_node == end:
            return cur_dist

        if cur_node[0] > 0:
            if ord(heightmap[cur_node[1]][cur_node[0] - 1]) - ord(heightmap[cur_node[1]][cur_node[0]]) <= 1:
                heapq.heappush(q, (cur_dist + 1, (cur_node[0] - 1, cur_node[1])))
        if cur_node[0] < len(heightmap[0]) - 1:
            if ord(heightmap[cur_node[1]][cur_node[0] + 1]) - ord(heightmap[cur_node[1]][cur_node[0]]) <= 1:
                heapq.heappush(q, (cur_dist + 1, (cur_node[0] + 1, cur_node[1])))
        if cur_node[1] > 0:
            if ord(heightmap[cur_node[1] - 1][cur_node[0]]) - ord(heightmap[cur_node[1]][cur_node[0]]) <= 1:
                heapq.heappush(q, (cur_dist + 1, (cur_node[0], cur_node[1] - 1)))
        if cur_node[1] < len(heightmap) - 1:
            if ord(heightmap[cur_node[1] + 1][cur_node[0]]) - ord(heightmap[cur_node[1]][cur_node[0]]) <= 1:
                heapq.heappush(q, (cur_dist + 1, (cur_node[0], cur_node[1] + 1)))

    return sys.maxsize


def solve_part1(heightmap: list[list[str]]) -> int:
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)

    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            if heightmap[y][x] == "S":
                heightmap[y][x] = "a"
                start = (x, y)
            elif heightmap[y][x] == "E":
                heightmap[y][x] = "z"
                end = (x, y)

    return shortest_distance(start, end, heightmap)


def solve_part2(heightmap: list[list[str]]) -> int:
    starts: list[tuple[int, int]] = []
    end: tuple[int, int] = (0, 0)

    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            if heightmap[y][x] == "S":
                heightmap[y][x] = "a"
            if heightmap[y][x] == "a":
                starts.append((x, y))
            elif heightmap[y][x] == "E":
                heightmap[y][x] = "z"
                end = (x, y)

    distances: list[int] = []
    for start in starts:
        distances.append(shortest_distance(start, end, heightmap))

    return min(distances)
