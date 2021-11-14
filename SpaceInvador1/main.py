import pygame
import random
import math
from pygame import mixer

# Initialise
pygame.init()

# Screen
screen = pygame.display.set_mode((1366, 768))
# background
background = pygame.image.load('a415uP.jpeg').convert()
# background sound (bruhh star wars lets go)
mixer.music.load("Star-Wars.mp3")
mixer.music.play(-1)
# game over
game_over_text = pygame.font.Font('SFProDisplay.ttf', 64)
# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 700
playerY = 675
playerX_change = 0
# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_enemies = 6
for i in range(no_enemies):
    enemyImg.append(pygame.image.load('space-invaders-enemy.png'))
    enemyX.append(random.randint(10, 1300))
    enemyY.append(random.randint(0, 100))
    enemyX_change.append(0.4)
    enemyY_change.append(60)

# laser
# ready - no bullet on screen
# fire - bullet is moving
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 675
laserY_change = 1.5
laser_state = "ready"
# Score
score_value = 0
font = pygame.font.Font('SFProDisplay.ttf', 32)
textX = 10
textY = 10

def game_over():
    game_over_text = font.render('Game Over!',
                                 True,
                                 (255, 255, 255))
    screen.blit(game_over_text, (600, 350))
def show_score(x, y):
    score = font.render('Score: ' +
                        str(score_value),
                        True, (255, 255, 255))
    screen.blit(score, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_laser(x, y):
    global laser_state
    laser_state = 'fire'
    screen.blit(laserImg, (x + 16, y + 10))


def iscollision(enemyX, enemyY, laserX, laserY):

    distance = math.sqrt((math.pow(enemyX - laserX, 2))
                         + (math.pow(enemyY - laserY, 2)))
    if distance < 40:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print('Key pressed')
            if event.key == pygame.K_a:
                playerX_change = -0.9
            if event.key == pygame.K_d:
                playerX_change = 0.9
            if event.key == pygame.K_SPACE:
                if laser_state == 'ready':
                    laser_sound = mixer.Sound('laser-gun.mp3')
                    pygame.mixer.Sound.set_volume(laser_sound, 0.3)
                    laser_sound.play()
                    laserX = playerX
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change

    if playerX <= 10:
        playerX = 10
    elif playerX >= 1290:
        playerX = 1290

    for i in range(no_enemies):

        # Game over
        if enemyY[i] > 675:
            for j in range(no_enemies):
                enemyY[j] = 3000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 10:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1290:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # collision
        collision = iscollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            explosion_sound = mixer.Sound('explosion.mp3')
            explosion_sound.play()
            laserY = 675
            laser_state = 'ready'
            score_value += 10
            enemyX[i] = random.randint(10, 1300)
            enemyY[i] = random.randint(0, 100)

        enemy(enemyX[i], enemyY[i], i)
    # laser movement
    if laserY <= 10:
        laserY = 675
        laser_state = "ready"
    if laser_state == "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
