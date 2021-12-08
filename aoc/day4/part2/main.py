from aoc import get_puzzle
from aoc.day4.part2.parser import get_called_numbers, get_cards


def call(cards, numbers):
    winning_cards = cards.copy()
    for called in numbers:
        for card in winning_cards:
            card.mark(called)
        for card in winning_cards:
            if card.check() and len(winning_cards) > 1:
                try:
                    winning_cards.remove(card)
                except ValueError:
                    print('should not happen')
            elif card.check() and len(winning_cards) == 1:
                return card.bingo() * int(called)


if __name__ == '__main__':
    puzzle = get_puzzle(day=4)
    called_numbers = get_called_numbers(puzzle)
    cards = get_cards(puzzle)
    bingo = call(cards, called_numbers)
    print(f'{bingo=}')


