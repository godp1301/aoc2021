from aoc import get_puzzle


class Card:
    def __init__(self, numbers):
        self.numbers = [n for row in numbers for n in row.split(' ') if n != '']
        self.called = [False for _ in range(25)]

    def get_numbers(self):
        return self.numbers

    def get_called(self):
        return self.called

    def get_row(self, row_num):
        return [self.numbers[row_num * 5 + i] for i in range(5)]

    def get_column(self, col_num):
        return [self.numbers[i * 5 + col_num] for i in range(5)]

    def get_called_row(self, row_num):
        return [self.called[row_num * 5 + i] for i in range(5)]

    def get_called_column(self, col_num):
        return [self.called[i * 5 + col_num] for i in range(5)]

    def mark(self, number):
        try:
            self.called[self.numbers.index(number)] = True
        except ValueError:
            pass

    def check(self):
        if self.called.count(True) >= 5:
            for i in range(5):
                row = self.get_called_row(i)
                col = self.get_called_column(i)
                if row.count(True) == 5 or col.count(True) == 5:
                    return self.bingo()

    def bingo(self):
        uncalled_sum = 0
        for i, b in enumerate(self.called):
            if b:
                self.numbers[i] = 0

        for n in self.numbers:
            uncalled_sum += int(n)

        return uncalled_sum


def get_called_numbers(puzzle):
    return puzzle[0].split(',')


def get_cards(puzzle):
    unparsed_cards = puzzle[1:]
    return [Card(unparsed_cards[i*5:i*5+5]) for i in range(int(len(unparsed_cards) / 5))]


def call(cards, numbers):
    for called in numbers:
        for card in cards:
            card.mark(called)
            bingo = card.check()

            if bingo:
                return bingo * int(called)


if __name__ == '__main__':
    puzzle = get_puzzle(day=4)
    called_numbers = get_called_numbers(puzzle)
    cards = get_cards(puzzle)
    bingo = call(cards, called_numbers)
    print(f'{bingo=}')


