import unittest

from hamcrest import assert_that, is_

from aoc.day4.part2 import puzzle
from aoc.day4.part2.parser import get_called_numbers, get_cards


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.called_numbers = get_called_numbers(puzzle)
        self.cards = get_cards(puzzle)

    def test_parsing_called_numbers(self):
        assert_that(self.called_numbers,
                    is_(['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10', '16', '13', '6', '15',
                         '25', '12', '22', '18', '20', '8', '19', '3', '26', '1']))

    def test_parsing_the_first_card(self):
        assert_that(self.cards[0].get_numbers(), is_(['22', '13', '17', '11', '0',
                                                      '8', '2', '23', '4', '24',
                                                      '21', '9', '14', '16', '7',
                                                      '6', '10', '3', '18', '5',
                                                      '1', '12', '20', '15', '19']))

    def test_parsing_the_second_card(self):
        assert_that(self.cards[1].get_numbers(), is_(['3', '15', '0', '2', '22',
                                                      '9', '18', '13', '17', '5',
                                                      '19', '8', '7', '25', '23',
                                                      '20', '11', '10', '24', '4',
                                                      '14', '21', '16', '12', '6']))
