from aoc import get_puzzle


def solve(puzzle):
    inc_count = 0
    for i, v in enumerate(puzzle):
        if i + 1 < len(puzzle) and puzzle[i + 1] > v:
            inc_count = inc_count + 1
    return inc_count


if __name__ == '__main__':
    count = solve(get_puzzle(day=1))
    print(f'{count=}')

