import sys
from dataclasses import dataclass

import pygame

from signos import Pattern


SIZE = WIDTH, HEIGHT = 500, 500
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


def init():
    pygame.display.set_caption("Signos")
    board = pygame.image.load("public/board.jpg").convert()
    SCREEN.blit(board, (0, 0))
    pygame.display.flip()


def color_match(pos: tuple):
    x, y = pos
    for color in ScreenPos.ALL_COLORS:
        if x in color.x_range and y in color.y_range:
            return color.name


def write_pattern_on_screen(pattern: Pattern):
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(str(pattern), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT - 50)
    SCREEN.blit(text, textRect)
    pygame.display.update()


def start():
    pattern = Pattern()
    user_pattern = []

    write_pattern_on_screen(pattern)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # clicked = pygame.mouse.get_pressed()[0]
            clicked = event.type == pygame.MOUSEBUTTONDOWN
            if clicked:
                mouse_pos = pygame.mouse.get_pos()
                color = color_match(mouse_pos)
                print(color)
                if color:
                    user_pattern.append(color)
                    print(f"Pattern: {pattern}")
                    print(f"User pattern: {user_pattern}")
                    if len(user_pattern) == len(pattern):
                        if user_pattern != pattern:
                            print("You lose!")
                            print("Restarting")
                            pattern.reset()
                            init()
                            start()
                        else:
                            pattern.append()
                        user_pattern.clear()
            write_pattern_on_screen(pattern)


if __name__ == "__main__":
    init()
    start()
