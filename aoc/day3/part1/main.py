from aoc import get_puzzle
from aoc.day3 import gamma_rate_of


def epsilon_rate_of(gamma_rate):
    return gamma_rate.translate(gamma_rate.maketrans('10', '01'))


def power_consumption_of(gamma_rate, epsilon_rate):
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solve(puzzle):
    gamma_rate = gamma_rate_of(puzzle)
    epsilon_rate = epsilon_rate_of(gamma_rate)
    wattage = power_consumption_of(gamma_rate, epsilon_rate)
    print(f'{wattage=}')


if __name__ == '__main__':
    solve(get_puzzle(day=3))
