import unittest

from hamcrest import assert_that, is_

from aoc.day2.part2.main import AimingSubmarine


class TestAimingSubmarine(unittest.TestCase):
    def setUp(self) -> None:
        self.aiming_sub = AimingSubmarine()

    def test_initial_aiming(self):
        assert_that(self.aiming_sub.get_aim(), is_(0))

    def test_down_increases_aim(self):
        self.aiming_sub.down(5)
        assert_that(self.aiming_sub.aim, is_(5))

    def test_up_decreases_aim(self):
        self.aiming_sub.up(5)
        assert_that(self.aiming_sub.aim, is_(-5))

    def test_forward_increase_position_and_aim(self):
        self.aiming_sub.down(2)
        self.aiming_sub.forward(3)
        assert_that(self.aiming_sub.get_position(), is_(3))
        assert_that(self.aiming_sub.get_depth(), is_(6))

    def test_example(self):
        self.aiming_sub.forward(5)
        self.aiming_sub.down(5)
        self.aiming_sub.forward(8)
        self.aiming_sub.up(3)
        self.aiming_sub.down(8)
        self.aiming_sub.forward(2)

        assert_that(self.aiming_sub.get_position(), is_(15))
        assert_that(self.aiming_sub.get_depth(), is_(60))
