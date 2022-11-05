""" Simple PONG Game
										"""
import random
import pygame
from sys import exit

pygame.font.init()

HIGHT = 600
WIDTH = 800

HALF_HIGHT = HIGHT/2
HALF_WIDTH = WIDTH/2

SPEED_X = 7 * random.choice((1, -1))
SPEED_Y = 7 * random.choice((1, -1))
PLAYER_SPEED = 0
COMPUTER_SPEED = 7


player_score = 0
computer_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 42)


def ball_move():
	global SPEED_X, SPEED_Y, player_score, computer_score
	ball.x += SPEED_X
	ball.y += SPEED_Y
	if ball.top <= 0 or ball.bottom >= HIGHT:
		SPEED_Y *= -1
	if ball.left <= 0:
		player_score += 1
		ball_new()
	if ball.right >= WIDTH:
		computer_score += 1
		ball_new()
	if ball.colliderect(player) or ball.colliderect(computer):
		SPEED_X *= -1


def player_move():
	player.y += PLAYER_SPEED
	if player.top <= 0:
		player.top = 0
	if player.bottom >= HIGHT:
		player.bottom = HIGHT
		
		
def computer_move():
	if computer.top < ball.y:
		computer.top += COMPUTER_SPEED
	if computer.bottom > ball.y:
		computer.bottom -= COMPUTER_SPEED
	if computer.top <= 0:
		computer.top = 0
	if computer.bottom >= HIGHT:
		computer.bottom = HIGHT
		
		
def ball_new():
	global SPEED_X, SPEED_Y
	ball.center = (HALF_WIDTH, HALF_HIGHT)
	SPEED_Y *= random.choice((1, -1))
	SPEED_X *= random.choice((1, -1))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Funny PONG')
clock = pygame.time.Clock()

ball = pygame.Rect(HALF_WIDTH-15, HALF_HIGHT-15, 30, 30)
player = pygame.Rect(WIDTH-20, HALF_HIGHT - 70, 10, 140)
computer = pygame.Rect(10, HALF_HIGHT - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_gray = (200, 200, 200)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				PLAYER_SPEED += 7
			if event.key == pygame.K_UP:
				PLAYER_SPEED -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				PLAYER_SPEED -= 7
			if event.key == pygame.K_UP:
				PLAYER_SPEED += 7
		
	ball_move()
	player_move()
	computer_move()
	
	screen.fill(bg_color)
	pygame.draw.rect(screen, light_gray, player)
	pygame.draw.rect(screen, light_gray, computer)
	pygame.draw.ellipse(screen, light_gray, ball)
	pygame.draw.aaline(screen, light_gray, (HALF_WIDTH, 0), (HALF_WIDTH, HIGHT))
	
	player_text = game_font.render(f"{player_score}", False, light_gray)
	screen.blit(player_text, (410, 15))
	
	computer_text = game_font.render(f"{computer_score}", False, light_gray)
	screen.blit(computer_text, (360, 15))
	
	pygame.display.update()
	clock.tick(60)
