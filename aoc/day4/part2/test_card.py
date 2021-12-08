import unittest

from hamcrest import assert_that, is_

from aoc.day4.part2 import puzzle
from aoc.day4.part2.parser import get_cards


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.cards = get_cards(puzzle)

    def test_get_first_card_row(self):
        row = self.cards[0].get_row(0)
        assert_that(row, is_(['22', '13', '17', '11', '0']))

    def test_get_second_card_row(self):
        row = self.cards[0].get_row(1)
        assert_that(row, is_(['8', '2', '23', '4', '24']))

    def test_get_last_card_row(self):
        row = self.cards[0].get_row(4)
        assert_that(row, is_(['1', '12', '20', '15', '19']))

    def test_get_first_card_column(self):
        col = self.cards[0].get_column(0)
        assert_that(col, is_(['22', '8', '21', '6', '1']))

    def test_get_second_card_column(self):
        col = self.cards[0].get_column(1)
        assert_that(col, is_(['13', '2', '9', '10', '12']))

    def test_get_last_card_column(self):
        col = self.cards[0].get_column(4)
        assert_that(col, is_(['0', '24', '7', '5', '19']))

    def test_initial_called_numbers(self):
        assert_that(self.cards[0].get_called(), is_([False, False, False, False, False,
                                                     False, False, False, False, False,
                                                     False, False, False, False, False,
                                                     False, False, False, False, False,
                                                     False, False, False, False, False]))
