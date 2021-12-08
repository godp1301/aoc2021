from aoc.day4.part2.card import Card


def get_called_numbers(puzzle):
    return puzzle[0].split(',')


def get_cards(puzzle):
    unparsed_cards = puzzle[1:]
    return [Card(unparsed_cards[i*5:i*5+5]) for i in range(int(len(unparsed_cards) / 5))]

