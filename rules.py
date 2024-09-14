from collections import Counter
from die import Die

class Rules:
    def __init__(self) -> None:
        """This class should simply take in a set of dice and return the scores for each category"""
        self.category_values = {
            "ones": 1,
            "twos": 2,
            "threes": 3,
            "fours": 4,
            "fives": 5,
            "sixes": 6
        }

        self.categories = [
            "bonus",
            "par",
            "two pairs",
            "triples",
            "four-of-a-kind",
            "full house",
            "little ladder",
            "big ladder",
            "chance",
            "yatzy"]
        
        self.n_of_a_kind_values = {
            "two pairs": 2,
            "triples": 3,
            "four-of-a-kind": 4 
        }
        
    def _get_number_of_dice_with_value(self, value: int, dice: dict[int, Die]):
        dice_counter = self._count_values(dice)
        return dice_counter[value]
    
    def _get_highest_dice_multiple(self, multiple: int, dice_counter: Counter) -> dict[int, int]:
        multiples = {value: counter for value, counter in dice_counter.items() if counter >= multiple}
        max_value, counter = max(multiples.items(), key=lambda x: x[1])
        return max_value, counter

    def singles(self, singles_category: str, dice: dict[int, Die]) -> int:
        if singles_category not in [name for name in self.category_values.keys()]: raise ValueError("Invalid Category Value")
        value = self.category_values[singles_category]
        number_of_dice_with_n_value = self._get_number_of_dice_with_value(value, dice)
        return number_of_dice_with_n_value * value
    
    def bonus(self, singles: dict[str, int]):
        return 50 if sum([score for score in singles.values()]) > 63 else 0

    def par(self, dice: dict):
        return self._n_of_a_kind(dice, 2)

    def triple(self, dice: dict):
        return self._n_of_a_kind(dice, 3)
    
    def fourple(self, dice:dict): 
        return self._n_of_a_kind(dice, 4)
    
    def _n_of_a_kind(self, dice:dict, n: int) -> int:
        dice_counter = self._count_values(dice)
        value, counter = self._get_highest_dice_multiple(n, dice_counter)
        return value * counter

    def full_house(self, dice: dict):
        dice_counter = self._count_values(dice)
        if 3 in dice_counter.values() and 2 in dice_counter.values():
            sum = 0
            value, counter = self._get_highest_dice_multiple(3, dice_counter)
            sum += value * counter
            dice_counter.subtract({value: counter})
            value1, counter1 = self._get_highest_dice_multiple(2, dice_counter)
            sum += value1 * counter1
            dice_counter.subtract({value1, counter1})
            return sum
        return 0
    
    def little_ladder(self, dice):
        values = self._get_dice_values(dice)
        return 15 if {1,2,3,4,5}.issubset(values) else 0

    def large_ladder(self, dice):
        values = self._get_dice_values(dice)
        return 20 if {2,3,4,5,6}.issubset(values) else 0

    def _get_dice_values(self, dice):
        return {die.value for die in dice.values()}
    
    def _count_values(self, dice: dict):
        return Counter([dice.value for dice in dice.values()])
    