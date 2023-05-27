import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks")

bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100
bat_rect[0] = screen.get_width() / 2 - bat_rect[2] / 2

ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (
bat_rect[0] + bat_rect[2] / 2 - ball.get_width() / 2, bat_rect[1] - bat_rect[3] / 2 - ball.get_height() / 2)
ball_speed = (-0.3, -0.4)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()

bricks = []
bricks_rows = 3
brick_gap = 10
bricks_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * bricks_cols + brick_gap) // 2

for y in range(bricks_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(bricks_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()
game_over = False
x = bat_rect[0]
while not game_over:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)
    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True

    if bat_rect.x + bat_rect.width >= ball_rect.x >= bat_rect.x and ball_rect.y + ball_rect.height >= bat_rect.y and sy > 0:
        sy *= -1
        sx *= 1.01
        sy *= 1.01
        continue

    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] + ball_rect.width/2 <= bx + brick_rect.width and by <= ball_rect[1] + ball_rect.height/2 <= by + brick_rect.height:
            delete_brick = b
            if ball_rect.x <= bx + 2:
                sx *= -1
            elif ball_rect.x >= bx + brick_rect.width - 2:
                sx *= -1
            if ball_rect.y <= by + 2:
                sy *= -1
            elif ball_rect.y >= by + brick_rect.height - 2:
                sy *= -1
            break
    if delete_brick is not None:
        bricks.remove(delete_brick)
    # Top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1

    # Bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_rect.topleft = ball_start
        sy, sx = ball_speed
        ball_served = False

    # Left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
        print(sx)

    # Right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    x = max(min(x, screen.get_width() - bat_rect.width), 0)
    bat_rect[0] = x
    if ball_served:
        ball_rect[0] += sx * dt
        ball_rect[1] += sy * dt
    pygame.display.update()
pygame.quit()
