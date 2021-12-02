from hamcrest import assert_that, is_

from aoc.day1.am.main import solve


def test_example():
    assert_that(solve([607, 618, 618, 617, 647, 716, 769, 792]), is_(5))
