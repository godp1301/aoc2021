from hamcrest import assert_that, is_

from aoc.day4.part1.main import get_called_numbers, get_cards, call, Card

puzzle = [
    '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '22 13 17 11  0',
    '8  2 23  4 24',
    '21  9 14 16  7',
    '6 10  3 18  5',
    '1 12 20 15 19',
    '3 15  0  2 22',
    '9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    '2  0 12  3  7'
]


def test_parsing_called_numbers():
    called_numbers = get_called_numbers(puzzle)
    assert_that(called_numbers,
                is_(['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10', '16', '13', '6', '15', '25', '12', '22', '18', '20', '8', '19', '3', '26', '1']))


def test_parsing_the_first_card():
    cards = get_cards(puzzle)
    assert_that(cards[0].get_numbers(), is_(['22', '13', '17', '11', '0',
                                             '8', '2', '23', '4', '24',
                                             '21', '9', '14', '16', '7',
                                             '6', '10', '3', '18', '5',
                                             '1', '12', '20', '15', '19']))


def test_parsing_the_second_card():
    cards = get_cards(puzzle)
    assert_that(cards[1].get_numbers(), is_(['3', '15', '0', '2', '22',
                                             '9', '18', '13', '17', '5',
                                             '19', '8', '7', '25', '23',
                                             '20', '11', '10', '24', '4',
                                             '14', '21', '16', '12', '6']))


def test_get_first_card_row():
    cards = get_cards(puzzle)
    row = cards[0].get_row(0)
    assert_that(row, is_(['22', '13', '17', '11', '0']))


def test_get_second_card_row():
    cards = get_cards(puzzle)
    row = cards[0].get_row(1)
    assert_that(row, is_(['8', '2', '23', '4', '24']))


def test_get_last_card_row():
    cards = get_cards(puzzle)
    row = cards[0].get_row(4)
    assert_that(row, is_(['1', '12', '20', '15', '19']))


def test_get_first_card_column():
    cards = get_cards(puzzle)
    col = cards[0].get_column(0)
    assert_that(col, is_(['22', '8', '21', '6', '1']))


def test_get_second_card_column():
    cards = get_cards(puzzle)
    col = cards[0].get_column(1)
    assert_that(col, is_(['13', '2', '9', '10', '12']))


def test_get_last_card_column():
    cards = get_cards(puzzle)
    col = cards[0].get_column(4)
    assert_that(col, is_(['0', '24', '7', '5', '19']))


def test_initial_called_numbers():
    cards = get_cards(puzzle)
    assert_that(cards[0].get_called(), is_([False, False, False, False, False,
                                            False, False, False, False, False,
                                            False, False, False, False, False,
                                            False, False, False, False, False,
                                            False, False, False, False, False]))


def test_calling_a_number():
    card = Card(['22', '13', '17', '11', '0',
                 '8', '2', '23', '4', '24',
                 '21', '9', '14', '16', '7',
                 '6', '10', '3', '18', '5',
                 '1', '12', '20', '15', '19'])

    call([card], ['22'])

    assert_that(card.get_called(), is_([True, False, False, False, False,
                                        False, False, False, False, False,
                                        False, False, False, False, False,
                                        False, False, False, False, False,
                                        False, False, False, False, False]))


def test_getting_a_bingo():
    card = Card(['14', '21', '17', '24', '4',
                 '10', '16', '15', '9', '19',
                 '18', '8', '23', '26', '20',
                 '22', '11', '13', '6', '5',
                 '2', '0', '12', '3', '7'])

    call([card], ['9', '23', '11', '5', '2', '0', '7', '14', '21', '17', '24', '4', ])
    bingo = card.check()
    assert_that(bingo, is_(188))


def test_example():
    called_numbers = get_called_numbers(puzzle)
    cards = get_cards(puzzle)
    bingo = call(cards, called_numbers)
    assert_that(bingo, is_(4512))
