from random import choice


class Action:
    GREEN = "Green"
    RED = "Red"
    YELLOW = "Yellow"
    BLUE = "Blue"
    ALL_ACTIONS = [GREEN, RED, YELLOW, BLUE]


class Pattern(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.append()

    def append(self):
        super().append(choice(Action.ALL_ACTIONS))

    def __str__(self):
        return " -> ".join(self)

    def reset(self):
        self.clear()
