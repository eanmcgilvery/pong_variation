import pygame
import sys
import random
import time
import random
from pygame.math import Vector2
from pygame.locals import *

def move_ball(self):
    self.x += self.velocity
    self.y += self.angle


pygame.init()
main_clock = pygame.time.Clock()

# Setup a Window
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1200
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Pong - No Walls!')
font = pygame.font.SysFont(None, 24)

# Setup Background color
DIM_GREY = Color('#3c3c3c')
WHITE = (255, 255, 255)
window_surface.fill(DIM_GREY)

# Setup movement Keys/Speed
MOVE_SPEED = 5

move_left = False
move_right = False
move_up = False
move_down = False

# Setup Player Paddles

PADDLE_R_HEIGHT = 180
PADDLE_R_WIDTH = 90

PADDLE_HEIGHT = 90
PADDLE_WIDTH = 180

BALL_WIDTH = 70
BALL_HEIGHT = 70

player_point = 0
computer_point = 0

player_right_paddle_image = pygame.image.load('PLAYER_PAD.png')
player_stretched_right_paddle = pygame.transform.scale(player_right_paddle_image, (PADDLE_R_WIDTH, PADDLE_R_HEIGHT))
player_right_rect = player_right_paddle_image.get_rect()
player_right_rect.center = (WINDOW_WIDTH + PADDLE_R_WIDTH / 4, WINDOW_HEIGHT / 2)

player_top_paddle_image = pygame.image.load('PLAYER_PAD2.png')
player_top_rect = player_top_paddle_image.get_rect()
player_stretched_top_paddle = pygame.transform.scale(player_top_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
player_top_rect.center = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 4, PADDLE_HEIGHT / 2)

player_bottom_paddle_image = pygame.image.load('PLAYER_PAD2.png')
player_bottom_rect = player_bottom_paddle_image.get_rect()
player_stretched_bottom_paddle = pygame.transform.scale(player_bottom_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
player_bottom_rect.center = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 4, WINDOW_HEIGHT + PADDLE_HEIGHT / 4)

computer_left_paddle_image = pygame.image.load('PLAYER_PAD.png')
computer_left_rect = computer_left_paddle_image.get_rect()
computer_stretched_left_paddle = pygame.transform.scale(computer_left_paddle_image, (PADDLE_R_WIDTH, PADDLE_R_HEIGHT))
computer_left_rect.center = (PADDLE_R_WIDTH / 2, WINDOW_HEIGHT / 2)

computer_top_paddle_image = pygame.image.load('PLAYER_PAD2.png')
computer_top_rect = player_top_paddle_image.get_rect()
computer_stretched_top_paddle = pygame.transform.scale(player_top_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
computer_top_rect.center = (WINDOW_WIDTH / 4, PADDLE_HEIGHT / 2)

computer_bottom_paddle_image = pygame.image.load('PLAYER_PAD2.png')
computer_bottom_rect = player_bottom_paddle_image.get_rect()
computer_stretched_bottom_paddle = pygame.transform.scale(player_bottom_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
computer_bottom_rect.center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT + PADDLE_HEIGHT / 4)

ball_image = pygame.image.load('ball.png')
ball_rect = ball_image.get_rect()
ball_stretched = pygame.transform.scale(ball_image, (BALL_WIDTH, BALL_HEIGHT))
ball_rect.center = (WINDOW_WIDTH / 2 + BALL_WIDTH, WINDOW_HEIGHT / 2 + BALL_HEIGHT)

# Setup Sounds
collision_sound = pygame.mixer.Sound('hit.wav')

random.seed(time)
ball_start = random.randint(1, 6)

play_again = True
while play_again:
    window_surface.fill(DIM_GREY)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Gather Key input from user
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                move_left = True
                move_right = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = True
                move_left = False
            if event.key == K_UP or event.key == K_w:
                move_up = True
                move_down = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = True
                move_up = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False

    # Right paddle vertical movement
    if move_down and player_right_rect.bottom <= WINDOW_HEIGHT:
        player_right_rect.top += MOVE_SPEED
    if move_up and player_right_rect.top > -20:
        player_right_rect.top -= MOVE_SPEED

    # Top and Bottom paddle Horizontal Movement
    if move_right and player_bottom_rect.right <= WINDOW_WIDTH:
        player_top_rect.right += MOVE_SPEED
        player_bottom_rect.right += MOVE_SPEED
    if move_left and player_bottom_rect.left >= WINDOW_WIDTH / 2:
        player_top_rect.right -= MOVE_SPEED
        player_bottom_rect.right -= MOVE_SPEED

    # Ball movement
    if ball_start == 1:
        ball_rect.top -= MOVE_SPEED
        ball_rect.right += MOVE_SPEED
    elif ball_start == 2:
        ball_rect.top += MOVE_SPEED
        ball_rect.right += MOVE_SPEED
    elif ball_start == 3:
        ball_rect.top += MOVE_SPEED
        ball_rect.right -= MOVE_SPEED
    elif ball_start == 4:
        ball_rect.right -= MOVE_SPEED
    elif ball_start == 5:
        ball_rect.right += MOVE_SPEED
    else:
        ball_rect.top -= MOVE_SPEED
        ball_rect.right -= MOVE_SPEED

    # Check for collisions
    if player_top_rect.colliderect(ball_rect):
        ball_rect.top -= MOVE_SPEED
    # collision_sound.play()
    if computer_top_rect.colliderect(ball_rect):
        ball_rect.top -= MOVE_SPEED
        # collision_sound.play()
    if computer_bottom_rect.colliderect(ball_rect):
        ball_rect.top += MOVE_SPEED
    # collision_sound.play()
    if player_bottom_rect.colliderect(ball_rect):
        ball_rect.top += MOVE_SPEED
        # collision_sound.play()
    if player_right_rect.colliderect(ball_rect):
        ball_rect.left -= MOVE_SPEED
    if computer_left_rect.colliderect(ball_rect):
        ball_rect.left += MOVE_SPEED

    # Computer Paddle AI
    if ball_rect.center > computer_left_rect.center and computer_left_rect.top > 0:
        computer_left_rect.top += MOVE_SPEED
    if ball_rect.midleft > computer_top_rect.center and computer_top_rect.right < WINDOW_WIDTH / 2:
        computer_top_rect.left += MOVE_SPEED
        computer_bottom_rect.left += MOVE_SPEED
    if ball_rect.midleft < computer_top_rect.center and computer_top_rect.left > 0:
        computer_top_rect.left -= MOVE_SPEED
        computer_bottom_rect.left -= MOVE_SPEED
    if ball_rect.center < computer_left_rect.center and computer_left_rect.bottom > WINDOW_HEIGHT:
        computer_left_rect.top -= MOVE_SPEED

    if ball_rect.bottom > WINDOW_HEIGHT or ball_rect.bottom > WINDOW_WIDTH or ball_rect.bottom < 0:
        if ball_rect.bottom > int(WINDOW_HEIGHT / 2):
            player_point += 1
        else:
            computer_point += 1

    if computer_top_rect.right > WINDOW_WIDTH / 2:
        computer_top_rect
    scoreprint = "Computer 1: " + str(computer_point)
    text = font.render(scoreprint, 10, WHITE)
    textpos = (WINDOW_WIDTH / 4, PADDLE_HEIGHT + PADDLE_HEIGHT / 2)
    window_surface.blit(text, textpos)

    scoreprint = "Player: " + str(player_point)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 8, PADDLE_HEIGHT + PADDLE_HEIGHT / 2)
    window_surface.blit(text, textpos)

    # Display Paddles and Balls
    window_surface.blit(ball_stretched, ball_rect)
    window_surface.blit(player_stretched_right_paddle, player_right_rect)
    window_surface.blit(player_stretched_top_paddle, player_top_rect)
    window_surface.blit(player_stretched_bottom_paddle, player_bottom_rect)
    window_surface.blit(computer_stretched_left_paddle, computer_left_rect)
    window_surface.blit(computer_stretched_top_paddle, computer_top_rect)
    window_surface.blit(computer_stretched_bottom_paddle, computer_bottom_rect)

    pygame.display.update()
    main_clock.tick(60)
