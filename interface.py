import sys
from dataclasses import dataclass
from time import sleep

import pygame

from pattern import Pattern


SIZE = WIDTH, HEIGHT = 500, 500
time_point_drawn = 0.2
pygame.init()
SCREEN = pygame.display.set_mode(SIZE)


@dataclass
class ColorPoint:
    name: str
    x_range: range
    y_range: range


class ScreenPos:
    GREEN = ColorPoint("Green", range(66, 226), range(87, 251))
    RED = ColorPoint("Red", range(250, 406), range(88, 242))
    YELLOW = ColorPoint("Yellow", range(70, 224), range(271, 411))
    BLUE = ColorPoint("Blue", range(255, 406), range(271, 400))
    ALL_COLORS = [GREEN, RED, YELLOW, BLUE]


class Game:
    pattern = Pattern()

    def __init__(self):
        pygame.display.set_caption("Signos")
        board = pygame.image.load("public/board.jpg").convert()
        SCREEN.blit(board, (0, 0))
        pygame.display.flip()

    def color_match(self, pos: tuple):
        x, y = pos
        for color in ScreenPos.ALL_COLORS:
            if x in color.x_range and y in color.y_range:
                return color.name

    def write_pattern_on_screen(self, pattern: Pattern):
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(str(pattern), True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT - 50)
        SCREEN.blit(text, textRect)
        pygame.display.update()

    def reset(self):
        print("You lose!")
        print("Restarting")
        self.pattern.reset()
        self.__init__()
        self.start()

    def draw_rect_on_region(self, color_name: str):
        color = list(filter(lambda c: c.name == color_name, ScreenPos.ALL_COLORS))[0]
        rect = pygame.Rect(color.x_range.start, color.y_range.start, 150, 150)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect, 2)
        pygame.display.update()
        sleep(time_point_drawn)
        self.__init__()
        sleep(time_point_drawn)

    def start(self):
        user_pattern = []
        self.write_pattern_on_screen(self.pattern)
        points_printed = False
        while True:
            if not points_printed:
                for action in self.pattern:
                    self.draw_rect_on_region(action)
                    points_printed = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                clicked = event.type == pygame.MOUSEBUTTONDOWN
                if clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    color = self.color_match(mouse_pos)
                    if color:
                        user_pattern.append(color)
                        if len(user_pattern) == len(self.pattern):
                            if user_pattern != self.pattern:
                                self.reset()
                            else:
                                self.pattern.append()
                            points_printed = False
                            user_pattern.clear()
                self.write_pattern_on_screen(self.pattern)


if __name__ == "__main__":
    game = Game()
    game.start()
