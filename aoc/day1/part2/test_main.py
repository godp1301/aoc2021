from hamcrest import assert_that, is_

from aoc.day1.part2 import main


def test_can_get_first_sliding_window_total():
    assert_that(main.get_sliding_window_total([199, 200, 208]), is_([607]))


def test_sliding_the_sliding_window():
    assert_that(main.get_sliding_window_total([199, 200, 208, 210]), is_([607, 618]))


def test_sliding_the_sliding_window_to_the_end():
    assert_that(main.get_sliding_window_total([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]),
                is_([607, 618, 618, 617, 647, 716, 769, 792]))
