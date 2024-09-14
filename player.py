from die import Die
from rules import Rules
from collections import Counter

class Player:
    def __init__(self, number_of_die:int = 5) -> None:
        self.dice = {n+1: Die(name=str(n+1)) for n in range(number_of_die)}
        self.dice_names = [name for name in self.dice.keys()]
    
    def roll_die(self, *dice_names):
        dice = self._get_dice_from_names(*dice_names)
        for die in dice:
            die.roll()

    def print_dice_values(self, *dice_names: int):
        dice = self._get_dice_from_names(*dice_names)
        for die in dice:
            print(die)

    def _get_dice_from_names(self, *dice_names: int) -> list[Die]:
        return [self.dice[dice_name] for dice_name in dice_names] if dice_names else self.dice.values()
    

if __name__ == "__main__":
    player = Player()
    player.roll_die()
    player.print_dice_values()
    print(player.get_number_of_dice_with_value(2))

