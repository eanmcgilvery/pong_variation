import pygame
import sys
import random
import time
import random
from pygame.math import Vector2
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

def vector2(xy_tuple, scale):
    v = Vector2()
    v[0], v[1] = xy_tuple[0], xy_tuple[1]
    return v * scale


def end_game():
    pygame.quit()
    sys.exit()


def scoreboard_update(player_game_score, computer_game_score, player_match_score, computer_match_score):
    # Create out font
    scoreboard_font = pygame.font.SysFont(None, 48)

    # Create the individual scoreboard for the game
    player_game_scoreboard = scoreboard_font.render('Game Score:' + str(player_game_score), 1, WHITE)
    computer_game_score = scoreboard_font.render('Game Score: ' + str(computer_game_score), 1, WHITE)

    # Create the individual scoreboard for the overall match
    player_match_scoreboard = scoreboard_font.render('Match Score: ' + str(player_match_score), 1, WHITE)
    computer_match_score = scoreboard_font.render('Match Score: ' + str(computer_match_score), 1, WHITE)

    # Put game scores on screen
    window_surface.blit(player_match_scoreboard, (WINDOW_WIDTH - 10, 175))
    window_surface.blit(player_game_scoreboard, (WINDOW_WIDTH - 10, 155))

    window_surface.blit(computer_match_score, (WINDOW_WIDTH - 1390, 175))
    window_surface.blit(computer_game_score, (WINDOW_WIDTH - 1390, 155))


# Setup the Window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

# Setup White for scoreboard colour
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window_surface.fill(WHITE)



#Setup Movement

move_left = False
move_right = False
move_up = False
move_down = False

COMP_MOVE_SPEED = 10


# Set Window caption
def play():
    pygame.display.set_caption('Pong No Walls')

    pygame.mouse.set_visible(False)

    font = pygame.font.Font(None, 48)

    # Create the Rectangles for the paddles
    player_image = pygame.image.load('player_paddle.png')
    player_right_paddle_rect = player_image.get_rect()
    computer_image = pygame.image.load('computer_paddle.png')
    computer_left_paddle_rect = computer_image.get_rect()

    computer_game_score = 0
    computer_match_score = 0
    player_game_score = 0
    player_match_score = 0

    play_again = True
    while play_again:
        for event in pygame.event.get():
            if event.type == QUIT:
                end_game()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    end_game()
    window_surface.blit(player_image, player_right_paddle_rect)
    window_surface.blit(computer_image, computer_left_paddle_rect)

    window_surface.fill(WHITE)
    scoreboard_update(player_game_score, computer_game_score, player_match_score, computer_match_score)


play()
