from aoc import get_puzzle
from aoc.day2 import solve
from aoc.day2.part1.main import Submarine


class AimingSubmarine(Submarine):
    def __init__(self):
        super(AimingSubmarine, self).__init__()
        self.aim = 0

    def get_aim(self):
        return self.aim

    def down(self, units):
        self.aim += units

    def up(self, units):
        self.aim -= units

    def forward(self, units):
        super().forward(units)
        self.depth += self.aim * units


if __name__ == '__main__':
    multiple = solve(get_puzzle(day=2), AimingSubmarine())
    print(f'{multiple=}')
