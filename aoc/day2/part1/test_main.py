import unittest

from hamcrest import assert_that, is_

from aoc.day2.part1.main import Submarine, solve


class TestSubmarine(unittest.TestCase):
    def setUp(self) -> None:
        self.sub = Submarine()

    def test_initial_distance(self):
        assert_that(self.sub.get_distance(), is_(0))

    def test_initial_depth(self):
        assert_that(self.sub.get_depth(), is_(0))

    def test_can_move_forward(self):
        self.sub.forward(5)
        assert_that(self.sub.get_distance(), is_(5))
        assert_that(self.sub.get_depth(), is_(0))

    def test_can_dive(self):
        self.sub.down(3)
        assert_that(self.sub.get_depth(), is_(3))
        assert_that(self.sub.get_distance(), is_(0))

    def test_can_surface(self):
        self.sub.down(3)
        self.sub.up(1)
        assert_that(self.sub.get_depth(), is_(2))
        assert_that(self.sub.get_distance(), is_(0))

    def test_example(self):
        self.sub.forward(5)
        self.sub.down(5)
        self.sub.forward(8)
        self.sub.up(3)
        self.sub.down(8)
        self.sub.forward(2)

        assert_that(self.sub.get_distance(), is_(15))
        assert_that(self.sub.get_depth(), is_(10))

    def test_example_with_parsing(self):
        multiple = solve([
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2']
        )

        assert_that(multiple, is_(150))
