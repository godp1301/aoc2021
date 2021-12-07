from hamcrest import is_, assert_that

from aoc.day3 import gamma_rate_of, most_common_bit_of


def test_equality_returns_one():
    assert_that(most_common_bit_of(['0', '1']), is_('1'))


def test_example_oxygen_rating():
    puzzle = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010'
    ]

    puzzle_copy = puzzle.copy()
    gamma_rate = gamma_rate_of(puzzle)
    for i, b in enumerate(gamma_rate):
        for e in puzzle:
            if e[i] != b and e in puzzle_copy:
                puzzle_copy.remove(e)

    assert_that(len(puzzle_copy), is_(1))
    assert_that('10111' in puzzle_copy, is_(True))
