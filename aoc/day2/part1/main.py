from aoc import get_puzzle
from aoc.day2 import solve


class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def get_position(self):
        return self.position

    def get_depth(self):
        return self.depth

    def forward(self, units):
        self.position += units

    def down(self, units):
        self.depth += units

    def up(self, units):
        self.depth -= units


if __name__ == '__main__':
    multiple = solve(get_puzzle(day=2), Submarine())
    print(f'{multiple=}')
