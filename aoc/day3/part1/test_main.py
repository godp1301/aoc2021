from hamcrest import assert_that, is_

from aoc.day3.part1.main import gamma_rate_of, epsilon_rate_of, power_consumption_of


def test_single_zero():
    assert_that(gamma_rate_of(['0']), is_('0'))


def test_single_one():
    assert_that(gamma_rate_of(['1']), is_('1'))


def test_multiple_zeros():
    assert_that(gamma_rate_of(['0', '0']), is_('0'))


def test_multiple_ones():
    assert_that(gamma_rate_of(['1', '1']), is_('1'))


def test_epsilon_rate_of():
    assert_that(epsilon_rate_of('10110'), is_('01001'))


def test_power_consumption_of():
    assert_that(power_consumption_of('10110', '01001'), is_(198))


def test_example():
    example = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010'
    ]
    gamma_rate = gamma_rate_of(example)
    assert_that(gamma_rate, is_('10110'))
    print()
