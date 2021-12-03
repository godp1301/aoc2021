from aoc import get_puzzle


def most_common_bit_of(values):
    return '0' if len([b for b in values if b == '0']) > len([b for b in values if b == '1']) else '1'


def gamma_rate_of(binary_numbers):
    mcb = []
    for i, v in enumerate(binary_numbers):
        mcb.append([b for b in v])

    v_list = list(zip(*mcb))
    return "".join([most_common_bit_of(v) for v in v_list])


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
