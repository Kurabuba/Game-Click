import pygame
import random
import time


pygame.init()

lav = (230, 230, 250)
thistle = (216, 191, 216)
plum = (221, 160, 221)
black = (0, 0, 0)
yellow = (0, 128, 128)
red = (255, 0, 0)
green = (0, 255, 51)
"""
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 51)
orange = (255, 123, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
lgreen = (200, 255, 200)
lred = (250, 128, 114)
black = (0, 0, 0)
dblue = (0, 0, 100)
lblue = (150, 150, 255)
"""

window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()


class Area():
    def __init__(self, x, y, width, hight, color=None):
        self.rect = pygame.Rect(x, y, width, hight)
        self.color = color

    def color_change(self, new_color):
        self.color = new_color

    def draw_rect(self):
        pygame.draw.rect(window, self.color, self.rect)

    def collide(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, size, color):
        font = pygame.font.Font(None, size)
        self.image = font.render(text, True, color)

    def draw_label(self, shift_x, shift_y):
        self.draw_rect()
        window.blit(self.image, [self.rect.x + shift_x, self.rect.y + shift_y])


cards = []
x = 20
for i in range(4):
    rect1 = Label(x, 100, 80, 150, yellow)
    rect1.set_text("", 40, black)
    cards.append(rect1)
    x += 130

score = 0

start_time = time.time()

printScore = Label(400, 30, 0, 0, black)
printTime = Label(50, 30, 0, 0, black)

wait = 0

gameRun = True

while gameRun:
    time_frame = time.time()
    time_passed = int(time_frame - start_time)
    window.fill(lav)
    printScore.set_text("Счет:" + str(score), 30, black)
    printScore.draw_label(0, 0)
    printTime.set_text("Время:" + str(time_passed), 30, black)
    printTime.draw_label(0, 0)
    for i in cards:
        i.draw_label(2, 60)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for card in cards:
                if card.collide(x, y):
                    if card == cards[rand_card]:
                        card.color_change(green)
                        score += 1
                    else:
                        card.color_change(red)
                        score -= 1
        elif event.type == pygame.QUIT:
            gameRun = False
            break


    wait -= 1
    if wait <= 0:
        wait = 60
        rand_card = random.randint(0, len(cards) - 1)
        for card in cards:
            card.color_change(yellow)
            card.set_text("", 30, black)
        cards[rand_card].set_text("CLICK", 35, black)

    if time_passed >= 10:
        printLose = Label(0, 0, 500, 500, red)
        printLose.set_text("Вы проиграли!", 70, black)
        printLose.draw_label(100, 90)
        #gameRun = False

    if score >= 5:
        printWin = Label(0, 0, 500, 500, green)
        printWin.set_text("Вы выиграли!", 70, black)
        printWin.draw_label(100, 90)
        #gameRun = False


    pygame.display.update()
    clock.tick(60)
