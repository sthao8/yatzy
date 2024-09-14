import unittest
from unittest.mock import Mock

from player import Die, Player
from rules import Rules


class TestRules(unittest.TestCase):
    def setUp(self) -> None:
        self.rules = Rules()

        return super().setUp()

    def test_1_singles_one_gives_1(self):
        dice = {"name" : Die("name", value=1)}
        self.assertEqual(
            self.rules.singles("ones", dice),
            1
        )

    def test_2_singles_none_gives_0(self):
        dice = {}
        self.assertEqual(
            self.rules.singles("ones", dice),
            0
        )

    def test_3_singles_multiple_gives_2(self):
        dice = {
            "name": Die("name", value=1),
            "name2": Die("name2", value=1)
            }
        self.assertEqual(
            self.rules.singles("ones", dice),
            2
        )

    def test_4_singles_works_with_other_values(self):
        dice = {
            "name": Die("name", value=5),
            "name2": Die("name2", value=5),
            "name3": Die("name3", value=5),
            "name4": Die("name4", value=5),
            "name5": Die("name5", value=5)
            }
        self.assertEqual(
            self.rules.singles("fives", dice),
            25
        )

    def test_5_bonus_returns_50_if_higher_than_63(self):
        singles = {
            "ones": 5,
            "twos": 10,
            "threes": 15,
            "fours": 20,
            "fives": 25,
            "sixes": 30
        }
        self.assertEqual(
            self.rules.bonus(singles),
            50
        )
    
    def test_6_bonus_returns_50_if_higher_than_63(self):
        singles = {
            "ones": 0,
            "twos": 0,
            "threes": 0,
            "fours": 0,
            "fives": 0,
            "sixes": 0
        }
        self.assertEqual(
            self.rules.bonus(singles),
            0
        )

    def test_7_6_par_returns_12(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6)
        }
        self.assertEqual(
            self.rules.par(dice),
            12
        )

    def test_8_6_triple_returns_18(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6),
            "name3": Die("name3", value=6)
        }
        self.assertEqual(
            self.rules.triple(dice),
            18
        )

    def test_9_6_fourofakind_returns_24(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6),
            "name3": Die("name3", value=6),
            "name4": Die("name4", value=6)
        }
        self.assertEqual(
            self.rules.fourple(dice),
            24
        )
    
    def test_10_highest_fullhouse_returns_28(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6),
            "name3": Die("name3", value=6),
            "name4": Die("name4", value=5),
            "name5": Die("name5", value=5)
        }
        self.assertEqual(
            self.rules.full_house(dice),
            28
        )

    def test_11_little_ladder_returns_15(self):
        dice = {
            "name": Die("name", value=1),
            "name2": Die("name2", value=2),
            "name3": Die("name3", value=3),
            "name4": Die("name4", value=4),
            "name5": Die("name5", value=5)
        }
        self.assertEqual(
            self.rules.little_ladder(dice),
            15
        )
        
    def test_12_large_ladder_returns_20(self):
        dice = {
            "name": Die("name", value=2),
            "name2": Die("name2", value=3),
            "name3": Die("name3", value=4),
            "name4": Die("name4", value=5),
            "name5": Die("name5", value=6)
        }
        self.assertEqual(
            self.rules.large_ladder(dice),
            20
        )

    def test_13_chance_returns_30(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6),
            "name3": Die("name3", value=6),
            "name4": Die("name4", value=6),
            "name5": Die("name5", value=6)
        }
        self.assertEqual(
            self.rules.chance(dice),
            30
        )

    def test_14_yatzy_returns_50(self):
        dice = {
            "name": Die("name", value=6),
            "name2": Die("name2", value=6),
            "name3": Die("name3", value=6),
            "name4": Die("name4", value=6),
            "name5": Die("name5", value=6)
        }
        self.assertEqual(
            self.rules.yatzy(dice),
            50
        )


if __name__ == '__main__':
    unittest.main()