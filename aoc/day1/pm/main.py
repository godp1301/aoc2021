from aoc import get_puzzle
from aoc.day1.am.main import solve


def get_sliding_window_total(puzzle):
    return [sum(puzzle[i: i + 3]) for i in range(len(puzzle)) if i + 2 < len(puzzle)]


if __name__ == '__main__':
    sliding_window_sums = get_sliding_window_total(get_puzzle(day=1))
    count = solve(sliding_window_sums)
    print(f'{count=}')
