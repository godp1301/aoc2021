from hamcrest import assert_that, is_

from aoc.day4.part2 import puzzle
from aoc.day4.part2.main import call
from aoc.day4.part2.parser import get_cards, get_called_numbers


def test_last_winning_card():
    calling_numbers = get_called_numbers(puzzle)
    cards = get_cards(puzzle)
    sum = call(cards, calling_numbers)
    assert_that(sum, is_(1924))

