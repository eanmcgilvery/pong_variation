import pygame
import sys
import time
import random
from pygame.locals import *


def scoreboard(player_score, computer_score, player_matche, computer_match, player_need, computer_need):
    # Games won scoreboard
    scoreprint = "Computer: " + str(computer_score)
    text = font.render(scoreprint, 10, WHITE)
    textpos = (WINDOW_WIDTH / 4, PADDLE_HEIGHT + PADDLE_HEIGHT / 2)
    window_surface.blit(text, textpos)

    scoreprint = "Player: " + str(player_score)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 8, PADDLE_HEIGHT + PADDLE_HEIGHT / 2)
    window_surface.blit(text, textpos)

    # Matches won scoreboard
    matchprint = "Matches won: " + str(player_matche)
    text = font.render(matchprint, 1, WHITE)
    matchprint_pos = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 8, PADDLE_HEIGHT + PADDLE_HEIGHT / 2 + 50)
    window_surface.blit(text, matchprint_pos)

    matchprint = "Matches won: " + str(computer_match)
    text = font.render(matchprint, 1, WHITE)
    matchprint_pos = (WINDOW_WIDTH / 4, PADDLE_HEIGHT + PADDLE_HEIGHT / 2 + 50)
    window_surface.blit(text, matchprint_pos)

    # Matches Needed to win
    points_needed = "Points Needed: " + str(computer_need)
    text = font.render(points_needed, 1, WHITE)
    needed_pos = (WINDOW_WIDTH / 4, PADDLE_HEIGHT + PADDLE_HEIGHT / 2 + 100)
    window_surface.blit(text, needed_pos)

    points_needed = "Points Needed: " + str(player_need)
    text = font.render(points_needed, 1, WHITE)
    needed_pos = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 8, PADDLE_HEIGHT + PADDLE_HEIGHT / 2 + 100)
    window_surface.blit(text, needed_pos)


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

ball_rect_up = False
ball_rect_down = False
ball_rect_left = False
ball_rect_right = False

# Setup Player Paddles

PADDLE_R_HEIGHT = 180
PADDLE_R_WIDTH = 90

PADDLE_HEIGHT = 90
PADDLE_WIDTH = 180

BALL_WIDTH = 70
BALL_HEIGHT = 70

player_point = 0
computer_point = 0
player_matches = 0
computer_matches = 0
player_needed = 11
computer_needed = 11

winner = {False: 'player'}

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

# Initial Ball movement
random_start = random.randint(0, 3)
if random_start == 0:
    ball_rect_up = True
    ball_rect_right = True
elif random_start == 1:
    ball_rect_up = True
    ball_rect_left = True
elif random_start == 2:
    ball_rect_down = True
    ball_rect_right = True
else:
    ball_rect_down = True
    ball_rect_left = True

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

    # Check ball collisions
    if player_top_rect.colliderect(ball_rect):
        ball_rect_up = False
        ball_rect_down = True
        collision_sound.play()
    if computer_top_rect.colliderect(ball_rect):
        ball_rect_up = False
        ball_rect_down = True
        collision_sound.play()
    if computer_bottom_rect.colliderect(ball_rect):
        ball_rect_down = False
        ball_rect_up = True
        collision_sound.play()
    if player_bottom_rect.colliderect(ball_rect):
        ball_rect_down = False
        ball_rect_up = True
        collision_sound.play()
    if player_right_rect.colliderect(ball_rect):
        ball_rect_right = False
        ball_rect_left = True
        collision_sound.play()
    if computer_left_rect.colliderect(ball_rect):
        ball_rect_right = True
        ball_rect_left = False
        collision_sound.play()

    # Ball speed
    if ball_rect_up:
        ball_rect.top -= MOVE_SPEED
    if ball_rect_down:
        ball_rect.top += MOVE_SPEED
    if ball_rect_right:
        ball_rect.right += MOVE_SPEED
    if ball_rect_left:
        ball_rect.right -= MOVE_SPEED

    # Computer Paddle AI
    if ball_rect.top > computer_left_rect.top and computer_left_rect.bottom > 0:
        computer_left_rect.top += MOVE_SPEED
    if ball_rect.midleft > computer_top_rect.center and computer_top_rect.right < WINDOW_WIDTH / 2:
        computer_top_rect.left += MOVE_SPEED
        computer_bottom_rect.left += MOVE_SPEED
    if ball_rect.midleft < computer_top_rect.center and computer_top_rect.left > 0:
        computer_top_rect.left -= MOVE_SPEED
        computer_bottom_rect.left -= MOVE_SPEED
    if ball_rect.bottom < computer_left_rect.bottom and computer_left_rect.bottom > WINDOW_HEIGHT:
        computer_left_rect.top -= MOVE_SPEED

    # Collect game points and
    if ball_rect.bottom > WINDOW_HEIGHT or ball_rect.bottom > WINDOW_WIDTH or ball_rect.bottom < 0:
        if ball_rect.bottom > int(WINDOW_HEIGHT / 2):
            player_point += 1
        else:
            computer_point += 1

        if player_point == 11 and player_point >= 2 + computer_point:
            player_matches += 1
            if player_matches == 3:
                winner = "WINNER: PLAYER"
                replay = "Press \'Q\' to quit!"
                text2 = font.render(winner, 40, WHITE)
                winnerpos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                replaypos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)
                window_surface.blit(text2, winner)
                window_surface.blit(text2, replay)
                for event in pygame.event.get():
                    if event.key == K_p:
                        play_again = True
                        pygame.quit()
                        sys.exit()

        if computer_point == 11 and computer_point >= 2 + player_point:
            computer_matches += 1
            if computer_matches == 3:
                winner = "WINNER: COMPUTER"
                replay = "Press \'P\' to play again!"
                text2 = font.render(winner, 40, WHITE)
                winnerpos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                replaypos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)
                window_surface.blit(text2, winner)
                window_surface.blit(text2, replay)
                for event in pygame.event.get():
                    if event.key == K_p:
                        play_again = True
                        pygame.quit()
                        sys.exit()
        ball_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    scoreboard(player_point, computer_point, player_matches, computer_matches, player_needed, computer_needed)

    # Display Paddles and Balls
    # Display Middle Net
    for y in range(40, WINDOW_HEIGHT - 50, 50):
        pygame.draw.rect(window_surface, WHITE, (WINDOW_WIDTH // 2 - 5, y, 10, 30), 0)
    window_surface.blit(ball_stretched, ball_rect)
    window_surface.blit(player_stretched_right_paddle, player_right_rect)
    window_surface.blit(player_stretched_top_paddle, player_top_rect)
    window_surface.blit(player_stretched_bottom_paddle, player_bottom_rect)
    window_surface.blit(computer_stretched_left_paddle, computer_left_rect)
    window_surface.blit(computer_stretched_top_paddle, computer_top_rect)
    window_surface.blit(computer_stretched_bottom_paddle, computer_bottom_rect)

    pygame.display.update()
    main_clock.tick(60)
