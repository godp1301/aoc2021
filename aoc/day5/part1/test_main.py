from hamcrest import assert_that, is_

from aoc.day5.part1.main import get_hydrothermal_vents, parse_line_coordinates, count_intersections


def test_can_parse_line():
    line = parse_line_coordinates('0,1 -> 2,3')
    assert_that(line.x1, is_(0))
    assert_that(line.y1, is_(1))
    assert_that(line.x2, is_(2))
    assert_that(line.y2, is_(3))


def test_can_draw_a_horizontal_line():
    vents = get_hydrothermal_vents('0,0 -> 5,0')
    assert_that(vents[0][0], is_(1))
    assert_that(vents[1][0], is_(1))
    assert_that(vents[2][0], is_(1))
    assert_that(vents[3][0], is_(1))
    assert_that(vents[4][0], is_(1))


def test_can_draw_a_vertical_line():
    vents = get_hydrothermal_vents('1,0 -> 1,5')
    assert_that(vents[1][0], is_(1))
    assert_that(vents[1][1], is_(1))
    assert_that(vents[1][2], is_(1))
    assert_that(vents[1][3], is_(1))
    assert_that(vents[1][4], is_(1))


def test_can_draw_line_intersections():
    get_hydrothermal_vents('0,0 -> 5,0')
    vents = get_hydrothermal_vents('0,0 -> 0,5')
    
    assert_that(vents[0][0], is_(2))


def test_can_count_intersections():
    get_hydrothermal_vents('0,0 -> 5,0')
    get_hydrothermal_vents('0,0 -> 0,5')

    assert_that(count_intersections(), is_(1))
