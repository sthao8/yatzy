import random

class Die:
    def __init__(self, name: str, sides:int = 6, value: int= None) -> None:
        self.name = name
        self.sides = sides
        self.value = value

    def __str__(self) -> str:
        return f"Dice {self.name}: {self.value}"

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value