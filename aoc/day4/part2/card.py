class Card:
    def __init__(self, numbers):
        self.numbers = [n for row in numbers for n in row.split(' ') if n != '']
        self.called = [False for _ in range(25)]
        self.winning = False

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
            print(f'marking {number} in {self.numbers[0]}')
        except ValueError:
            pass

    def check(self):
        if self.called.count(True) >= 5:
            for i in range(5):
                row = self.get_called_row(i)
                col = self.get_called_column(i)
                if row.count(True) == 5 or col.count(True) == 5:
                    self.winning = True
                    return True

    def is_winning(self):
        return self.winning

    def bingo(self):
        uncalled_sum = 0
        for i, b in enumerate(self.called):
            if b:
                self.numbers[i] = 0

        for n in self.numbers:
            uncalled_sum += int(n)

        return uncalled_sum
