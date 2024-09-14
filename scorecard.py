from rules import Rules

rules = Rules()

class Scorecard:
    def __init__(self) -> None:
        self.columns = {category: 0 for category in rules.categories}

    def record_score(self, category: str, score: int):
        self.columns[category] = score