from aoc import get_puzzle


class Submarine:
    def __init__(self):
        self.distance = 0
        self.depth = 0

    def get_distance(self):
        return self.distance

    def get_depth(self):
        return self.depth

    def forward(self, units):
        self.distance += units

    def down(self, units):
        self.depth += units

    def up(self, units):
        self.depth -= units


def _get_unit(line):
    return int(line.split(' ')[1])


def solve(puzzle):
    submarine = Submarine()
    for move in puzzle:
        if 'forward' in move:
            submarine.forward(_get_unit(move))
        elif 'down' in move:
            submarine.down(_get_unit(move))
        elif 'up' in move:
            submarine.up(_get_unit(move))

    return submarine.get_distance() * submarine.get_depth()


if __name__ == '__main__':
    multiple = solve(get_puzzle(day=2))
    print(f'{multiple=}')
