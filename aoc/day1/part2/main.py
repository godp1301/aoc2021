from aoc import get_puzzle
from aoc.day1.part1.main import solve


def get_sliding_window_total(puzzle):
    return [sum(puzzle[i: i + 3]) for i in range(len(puzzle)) if i + 2 < len(puzzle)]


if __name__ == '__main__':
    puzzle = get_puzzle(day=1)
    sliding_window_sums = get_sliding_window_total([int(v) for v in puzzle])
    count = solve(sliding_window_sums)
    print(f'{count=}')
