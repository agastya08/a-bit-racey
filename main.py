import pygame
from pygame import mixer
import math
import random


pygame.init()
pygame.font.init()
Font = pygame.font.SysFont("freesansbold.ttf", 64)

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("A Bit Racey")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

carImg = pygame.image.load("car.png")

def car(x, y):
    screen.blit(carImg, (x, y))


def blue_enemy(x, y):
    blue_enemyImg = pygame.image.load("blue_enemy.png")
    screen.blit(blue_enemyImg, (x, y))


def yellow_enemy(x, y):
    yellow_enemyImg = pygame.image.load("yellow_enemy.png")
    screen.blit(yellow_enemyImg, (x, y))


blue_enemyX = random.randint(0, 736)
blue_enemyY = 0
blue_enemyY_change = 2

yellow_enemyX = random.randint(0, 736)
yellow_enemyY = -250
yellow_enemyY_change = 2

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
red = (255, 0, 0)

carX = 380
carY = 480
carX_change = 0
carY_change = 0


def bar1(x, y):
    barImg = pygame.image.load("road_bar.png")
    screen.blit(barImg, (x, y))


def bar2(x, y):
    barImg = pygame.image.load("road_bar.png")
    screen.blit(barImg, (x, y))


barX = 280
barY = 0
barY_change = 2

bar2X = 280
bar2Y = 400
bar2Y_change = 2

dodged = 0


def cars_dodged(count):
    dodged_font = pygame.font.Font('freesansbold.ttf', 25)
    text = dodged_font.render("Score: " + str(count), True, black)
    screen.blit(text, (10, 10))


def crashed():
    crash_sound = mixer.Sound("crash.mp3")
    crash_sound.play()

    crashed = True

    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.init()
        pygame.font.init()
        crashed_font = pygame.font.Font('freesansbold.ttf', 64)
        crashed_text = crashed_font.render("YOU CRASHED!", True, black)
        screen.blit(crashed_text, (180, 250))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, (0, 200, 0), (155, 400, 130, 50))
        pygame.draw.rect(screen, (255, 0, 0), (520, 400, 100, 50))

        button_font = pygame.font.Font('freesansbold.ttf', 20)
        start_text = button_font.render("Play Again", True, (0, 0, 0))
        screen.blit(start_text, (170, 415))

        quit_text = button_font.render("QUIT", True, (0, 0, 0))
        screen.blit(quit_text, (547, 415))

        cars_dodged(dodged)

        pygame.display.update()

        if 170 + 100 > mouse[0] > 170 and 400 + 50 > mouse[1] > 400:
            if click[0] == 1:
                mixer.music.load("bg_music.mp3")
                mixer.music.play(-1)
                crashed = False

        if 520 + 100 > mouse[0] > 520 and 400 + 50 > mouse[1] > 400:
            if click[0] == 1:
                pygame.quit()
                exit(0)


def black_enemy(x, y):
    black_enemyImg = pygame.image.load("black_enemy.png")
    screen.blit(black_enemyImg, (x, y))


black_enemyX = random.randint(50, 736)
black_enemyY = -700
black_enemyY_change = 2
black_enemyX_change = 2


def introduction():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen.fill(grey)
        background = pygame.image.load("intro_bg.png")
        screen.blit(background, (0, 0))

        mixer.music.load("bg_music.mp3")
        mixer.music.play(-1)

        # pygame.font.init()
        # Font = pygame.font.SysFont("freesansbold.ttf", 64)
        intro_font = pygame.font.Font('freesansbold.ttf', 64)
        controls_font = pygame.font.Font('freesansbold.ttf', 20)
        intro_text = intro_font.render("A BIT RACEY", True, white)
        control1 = controls_font.render("W- Move Forward", True, white)
        control2 = controls_font.render("A- Move Left", True, white)
        control3 = controls_font.render("S- Move Backwards", True, white)
        control4 = controls_font.render("D- Move Right", True, white)
        alert = controls_font.render("Enemy Speed Will Increase Every 50 Points!", True, red)
        screen.blit(intro_text, (200, 250))
        screen.blit(control1, (20, 20))
        screen.blit(control2, (20, 45))
        screen.blit(control3, (20, 70))
        screen.blit(control4, (20, 95))
        screen.blit(alert, (20, 120))

        pygame.draw.rect(screen, (0, 200, 0), (170, 400, 100, 50))
        pygame.draw.rect(screen, (255, 0, 0), (520, 400, 100, 50))

        button_font = pygame.font.Font('freesansbold.ttf', 20)
        start_text = button_font.render("START", True, (0, 0, 0))
        screen.blit(start_text, (189, 415))

        quit_text = button_font.render("QUIT", True, (0, 0, 0))
        screen.blit(quit_text, (542, 415))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 170 + 100 > mouse[0] > 170 and 400 + 50 > mouse[1] > 400:
            if click[0] == 1:
                intro = False

        pygame.display.update()

        if 520 + 100 > mouse[0] > 520 and 400 + 50 > mouse[1] > 400:
            if click[0] == 1:
                pygame.quit()
                exit(0)


def isCollision(enemyX, enemyY, carX, carY):
    distance = math.sqrt(math.pow(enemyX - carX, 2) + (math.pow(enemyY - carY, 2)))

    if distance < 56:
        return True
    else:
        return False


def round_off(x, base=50):
    return int(base * round(float(x) / base))


introduction()
running = True
while running:
    # print(pygame.font.get_fonts())
    # print(blue_enemyY_change)
    screen.fill(grey)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                carX_change -= 1.5
            if event.key == pygame.K_d:
                carX_change += 1.5
            if event.key == pygame.K_w:
                carY_change -= 1.5
            if event.key == pygame.K_s:
                carY_change += 1.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                carX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                carY_change = 0

    if barY >= 790:
        barY = 0

    if bar2Y >= 790:
        bar2Y = 0

    bar1(barX, barY)
    barY += barY_change

    bar2(bar2X, bar2Y)
    bar2Y += bar2Y_change

    car(carX, carY)
    carX += carX_change
    carY += carY_change

    blue_enemy(blue_enemyX, blue_enemyY)
    blue_enemyY += blue_enemyY_change

    if blue_enemyY >= 600:
        blue_enemyY = 0
        blue_enemyX = random.randint(0, 736)
        dodged += 1

    yellow_enemy(yellow_enemyX, yellow_enemyY)
    yellow_enemyY += yellow_enemyY_change

    if yellow_enemyY >= 600:
        yellow_enemyY = 0
        yellow_enemyX = random.randint(0, 736)
        dodged += 1

    black_enemy(black_enemyX, black_enemyY)
    black_enemyX += black_enemyX_change
    black_enemyY += black_enemyY_change

    if black_enemyY >= 600:
        black_enemyY = 0
        black_enemyX = random.randint(0, 736)
        dodged += 5

        if round_off(dodged) % 50 == 0 and dodged > 49 and dodged % 50 == 0:
            blue_enemyY_change += 0.5
            yellow_enemyY_change += 0.5
            black_enemyY_change += 0.5
            black_enemyX_change += 0.5
            barY_change += 0.3
            bar2Y_change += 0.3


    if black_enemyX >= 736:
        black_enemyX_change = -2

    if black_enemyX <= 0:
        black_enemyX_change = 2

    if carX >= 736:
        carX = 736
        mixer.music.stop()
        crashed()
        blue_enemyY_change = 0
        yellow_enemyY_change = 0
        barY_change = 0
        bar2Y_change = 0
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if carX <= 0:
        carX = 0
        mixer.music.stop()
        crashed()
        blue_enemyY_change = 0
        yellow_enemyY_change = 0
        barY_change = 0
        bar2Y_change = 0
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if carY >= 536:
        carY = 536
        mixer.music.stop()
        crashed()
        blue_enemyY_change = 0
        yellow_enemyY_change = 0
        barY_change = 0
        bar2Y_change = 0
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if carY <= 0:
        carY = 0
        mixer.music.stop()
        crashed()
        blue_enemyY_change = 0
        yellow_enemyY_change = 0
        barY_change = 0
        bar2Y_change = 0
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if isCollision(blue_enemyX, blue_enemyY, carX, carY):
        mixer.music.stop()
        crashed()
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if isCollision(yellow_enemyX, yellow_enemyY, carX, carY):
        mixer.music.stop()
        crashed()
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    if isCollision(black_enemyX, black_enemyY, carX, carY):
        mixer.music.stop()
        crashed()
        dodged = 0

        carX = 380
        carY = 480
        carX_change = 0
        carY_change = 0

        barX = 280
        barY = 0
        barY_change = 2

        bar2X = 280
        bar2Y = 400
        bar2Y_change = 2

        blue_enemyX = random.randint(0, 736)
        blue_enemyY = 0
        blue_enemyY_change = 2

        yellow_enemyX = random.randint(0, 736)
        yellow_enemyY = -250
        yellow_enemyY_change = 2

        black_enemyX = random.randint(50, 736)
        black_enemyY = -700
        black_enemyY_change = 2
        black_enemyX_change = 2

    cars_dodged(dodged)

    pygame.display.update()
