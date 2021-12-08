import re
from dataclasses import dataclass

rows, cols = (10, 10)
vents = [[0 for _ in range(cols)] for _ in range(rows)]


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int


def parse_line_coordinates(line):
    pattern = re.compile('(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)')
    match = pattern.search(line)
    x1 = int(match.group('x1'))
    y1 = int(match.group('y1'))
    x2 = int(match.group('x2'))
    y2 = int(match.group('y2'))

    return Line(x1, y1, x2, y2)


def get_hydrothermal_vents(puzzle):
    line = parse_line_coordinates(puzzle)
    line_length = max(abs(line.x1 - line.x2), abs(line.y1 - line.y2))

    if line.x1 < line.x2 and line.y1 == line.y2:
        for x in range(line_length):
            vents[line.x1 + x][line.y1] += 1
    elif line.y1 < line.y2 and line.x1 == line.x2:
        for y in range(line_length):
            vents[line.x1][line.y1 + y] += 1

    return vents


def count_intersections():
    intersections = 0
    for x in range(len(vents)):
        for y in range(len(vents[0])):
            if vents[x][y] > 1:
                intersections += 1

    return intersections
