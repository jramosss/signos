from dataclasses import dataclass
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


@dataclass
class Signos:
    pattern = Pattern()

    def start(self):
        while True:
            print(self.pattern)
            for action in self.pattern:
                user_input = str(input("Enter the color: "))
                if user_input != action:
                    print("You lose!")
                    print("Restarting")
                    self.pattern.reset()
                    self.start()
            self.pattern.append()


if __name__ == "__main__":
    signos = Signos()
    signos.start()
