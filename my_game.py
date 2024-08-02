# ======================================
# Ping Pong game Of St Cyr Vandersar   ||
# ======================================
import pygame
import sys
import random
from pygame import mixer
from math import cos, sin, radians

pygame.init()

# Colors
light_blue = (51, 102, 255)
blue = (0, 0, 255)
dark_blue = (0, 0, 102)
light_red = (255, 65, 65)
red = (255, 0, 0)
dark_red = (153, 0, 0)
light_green = (102, 255, 0)
green = (51, 153, 0)
dark_green = (0, 51, 0)
white = (255, 255, 255)
grey = (102, 102, 102)
black = (0, 0, 0)
yellow = (255, 255, 0)
orange = (255, 102, 0)
purple = (153, 0, 204)

# screen
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
# screen.fill(black)
BG = pygame.image.load("background.jpg")
default_size = (width, height)
BG = pygame.transform.scale(BG, default_size)

# Title & icon
pygame.display.set_caption("*Ping Pong Game*")
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

# music_background
mixer.music.load('music_bg.mp3')
mixer.music.play(-1)

clock = pygame.time.Clock()
margin = 4

scoreA = 0
scoreB = 0

moveA = 0
moveB = 0

# Paddle


class Paddle:
    def __init__(self, position):
        self.w = 10
        self.h = self.w * 8
        self.Speed = 6

        if position == -1:
            self.x = 1.5 * margin
        else:
            self.x = width - 1.5 * margin - self.w

        self.y = height / 2 - self.h / 2

    # Show the Paddle
    def show(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.w, self.h))

    # Move the Paddle
    def move(self, pixels):
        self.y += self.Speed * pixels
        if self.y < 0:
            self.y = 0
        elif self.y + self.h > height:
            self.y = height - self.h


PaddleA = Paddle(-1)
PaddleB = Paddle(1)

# Ball


class Ball:
    def __init__(self, image):
        self.r = 30
        self.x = width / 2 - self.r / 2
        self.y = height / 2 - self.r / 2
        self.image = image
        self.angle = random.randint(-75, 75)

        if random.randint(0, 1):
            self.angle += 180

        self.speed = 8

    # Show the Ball
    def show(self):
        screen.blit(self.image, (self.x, self.y))

    # Move the Ball
    def move(self):
        global scoreA, scoreB
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))

        if self.x - self.r > width - margin:
            scoreA += 1
            self.x = width / 2 - self.r / 2
            self.y = height / 2 - self.r / 2
            self.angle = 180 - self.angle

        if self.x + self.r < margin:
            scoreB += 1
            self.x = width / 2 - self.r / 2
            self.y = height / 2 - self.r / 2
            self.angle = self.angle - 180

        if self.y < margin:
            self.angle = - self.angle
        if self.y + self.r >= height - margin:
            self.angle = - self.angle

    # Check and Reflect the Ball when it hits the paddle
    def checkForPaddle(self):
        if self.x < width / 2:
            if PaddleA.x < self.x < PaddleA.x + PaddleA.w:
                if PaddleA.y < self.y < PaddleA.y + 10 or PaddleA.y < self.y + self.r < PaddleA.y + 10:
                    self.angle = -45
                if PaddleA.y + 10 < self.y < PaddleA.y + 20 or PaddleA.y + 10 < self.y + self.r < PaddleA.y + 20:
                    self.angle = -30
                if PaddleA.y + 20 < self.y < PaddleA.y + 30 or PaddleA.y + 20 < self.y + self.r < PaddleA.y + 30:
                    self.angle = -15
                if PaddleA.y + 30 < self.y < PaddleA.y + 40 or PaddleA.y + 30 < self.y + self.r < PaddleA.y + 40:
                    self.angle = -10
                if PaddleA.y + 40 < self.y < PaddleA.y + 50 or PaddleA.y + 40 < self.y + self.r < PaddleA.y + 50:
                    self.angle = 10
                if PaddleA.y + 50 < self.y < PaddleA.y + 60 or PaddleA.y + 50 < self.y + self.r < PaddleA.y + 60:
                    self.angle = 15
                if PaddleA.y + 60 < self.y < PaddleA.y + 70 or PaddleA.y + 60 < self.y + self.r < PaddleA.y + 70:
                    self.angle = 30
                if PaddleA.y + 70 < self.y < PaddleA.y + 80 or PaddleA.y + 70 < self.y + self.r < PaddleA.y + 80:
                    self.angle = 45
        else:
            if PaddleB.x + PaddleB.w > self.x + self.r > PaddleB.x:
                if PaddleB.y < self.y < PaddleA.y + 10 or PaddleA.y < self.y + self.r < PaddleA.y + 10:
                    self.angle = -135
                if PaddleB.y + 10 < self.y < PaddleB.y + 20 or PaddleB.y + 10 < self.y + self.r < PaddleB.y + 20:
                    self.angle = -150
                if PaddleB.y + 20 < self.y < PaddleB.y + 30 or PaddleB.y + 20 < self.y + self.r < PaddleB.y + 30:
                    self.angle = -165
                if PaddleB.y + 30 < self.y < PaddleB.y + 40 or PaddleB.y + 30 < self.y + self.r < PaddleB.y + 40:
                    self.angle = 170
                if PaddleB.y + 40 < self.y < PaddleB.y + 50 or PaddleB.y + 40 < self.y + self.r < PaddleB.y + 50:
                    self.angle = 190
                if PaddleB.y + 50 < self.y < PaddleB.y + 60 or PaddleB.y + 50 < self.y + self.r < PaddleB.y + 60:
                    self.angle = 165
                if PaddleB.y + 60 < self.y < PaddleB.y + 70 or PaddleB.y + 60 < self.y + self.r < PaddleB.y + 70:
                    self.angle = 150
                if PaddleB.y + 70 < self.y < PaddleB.y + 80 or PaddleB.y + 70 < self.y + self.r < PaddleB.y + 80:
                    self.angle = 135


BALL = pygame.image.load("ball.jpg")
size = 30
default_size_ball = (size, size)
trans_Ball = pygame.transform.scale(BALL, default_size_ball)
ball = Ball(trans_Ball)

# text for score


def afficheResult():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('Joueur_1: ' + str(scoreA), True, dark_red, black)
    text2 = font.render('Joueur_2: ' + str(scoreB), True, dark_red, black)

    screen.blit(text1, (60, 10))
    screen.blit(text2, (width // 2 + 300, 10))


def exit():
    pygame.quit()
    sys.exit()


def demarrer():
    global PaddleA, PaddleB, ball, moveA, moveB
    while True:
        screen.blit(BG, (0, 0))
        pygame.draw.line(screen, red, [width // 2, 0],
                         [width // 2, height], margin)
        pygame.draw.circle(screen, red, [width // 2, height // 2], 100, margin)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    exit()
                if event.key == pygame.K_q:
                    moveA = -2
                if event.key == pygame.K_z:
                    moveA = 2
                if event.key == pygame.K_UP:
                    moveB = -2
                if event.key == pygame.K_DOWN:
                    moveB = 2
            if event.type == pygame.KEYUP:
                moveA = 0
                moveB = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break

        PaddleA.move(moveA)
        PaddleB.move(moveB)

        PaddleB.show()
        PaddleA.show()

        ball.show()
        ball.move()
        ball.checkForPaddle()

        afficheResult()

        pygame.display.update()
        clock.tick(60)


demarrer()
