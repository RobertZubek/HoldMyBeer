import random
import pygame

butt_bg = pygame.image.load('beer_bg.jpeg')

pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hold my beer")

drink = pygame.mixer.Sound("drink.mp3")
jump = pygame.mixer.Sound("jump.mp3")
pygame.mixer.music.load("music.mp3")
lost_beer = pygame.mixer.Sound("-1.mp3")
lost = pygame.mixer.Sound("lost.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

gameInPause = False
gameLost = False
gameInMenu = True


def draw_text(text, font_1, color, a, b):
    img = font_1.render(text, True, color)
    win.blit(img, (a, b))


font = pygame.font.SysFont("arialblack", 40)
font1 = pygame.font.SysFont("arialblack", 20)
textColor = (255, 191, 0)

beer = pygame.image.load('beer.png')
beer1 = pygame.image.load('beer1.png')
beer2 = pygame.image.load('beer2.png')
character = pygame.image.load('character.png')
background = pygame.image.load('12492941.jpg')

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
x = 300
y = 490
objx = random.randint(10, 490)
objy = random.randint(-60, -20)
objx1 = random.randint(10, 490)
objy1 = random.randint(-60, -10)
objx2 = random.randint(10, 490)
objy2 = random.randint(-60, -20)
szer = 1
wys = 1
krok = 10
kroky = 0
wynik = 0
gamePace = 6
yPace = 6
y1Pace = 0
y2Pace = 0
promil = 0.1


run = True
while run:
    win.fill((0, 0, 0))
    win.blit(background, (-150, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameInPause = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if gameLost:
                    wynik = 0
                gameInMenu = False
                gameLost = False
                gameInPause = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                gameInMenu = True
                gameInPause = False
                x = 300
                y = 490
                objx = random.randint(10, 490)
                objy = random.randint(-60, -20)
                objx1 = random.randint(10, 490)
                objy1 = random.randint(-60, -20)
                objx2 = random.randint(10, 490)
                objy2 = random.randint(-60, -20)
                szer = 10
                wys = 10
                krok = 10
                kroky = 0
                wynik = 0
                gamePace = 3
                yPace = 3
                y1Pace = 0
                y2Pace = 0
                promil = 0.1
        if event.type == pygame.QUIT:
            run = False
    if gameInPause:
        gameInMenu = False
        draw_text("Press UP arrow to replay", font1, textColor, 130, 150)
        draw_text("Press M key to go to menu", font1, textColor, 120, 190)

    elif gameInMenu:
        gameInPause = False
        gameLost = False
        x = 300
        y = 490
        objx = random.randint(10, 490)
        objy = random.randint(-60, -20)
        objx1 = random.randint(10, 490)
        objy1 = random.randint(-60, -20)
        objx2 = random.randint(10, 490)
        objy2 = random.randint(-60, -20)
        szer = 10
        wys = 10
        krok = 10
        kroky = 0
        wynik = 0
        gamePace = 3
        yPace = 3
        y1Pace = 0
        y2Pace = 0
        promil = 0.1
        draw_text("Press  UP arrow to play", font1, textColor, 120, 150)
        draw_text("Press  Q key to exit", font1, textColor, 140, 190)

    elif gameLost:
        draw_text("Press  UP arrow to play again", font1, textColor, 120, 150)
        draw_text("Press  M key to go to menu", font1, textColor, 120, 190)
        draw_text("Press  Q key to exit", font1, textColor, 120, 240)
        draw_text(("Your score: " + str(wynik)), font1, textColor, 140, 110)

    else:

        draw_text(str(wynik), font, textColor, 250, 200)
        draw_text("‰:" + str(promil), font, textColor, 0, 450)

        pygame.time.delay(50)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x = x - krok
        if keys[pygame.K_RIGHT]:
            x = x + krok
        if y >= 478:
            if keys[pygame.K_SPACE]:
                kroky = 4
                pygame.mixer.Sound.play(jump)
        if x <= 0:
            x = 489
        if x >= 490:
            x = 0
        if y >= 478:
            y = 478
        if y <= 0:
            kroky = -9
        objy = objy + yPace
        objy1 = objy1 + y1Pace
        objy2 = objy2 + y2Pace
        y = y - kroky
        if abs(y - objy) < 15:
            if abs(objx - x) < 15:
                kroky = -4
                yPace += random.random()
                objy = random.randint(-60, -20)
                objx = random.randint(10, 490)
                if wynik > 10:
                    y1Pace += random.random()
                wynik += 1
                pygame.mixer.Sound.play(drink)
                promil += 0.1
        if abs(y - objy1) < 15:
            if abs(objx1 - x) < 15:
                kroky = -4
                y1Pace += random.random()
                objy1 = random.randint(-60, -20)
                objx1 = random.randint(10, 490)
                if wynik > 20:
                    y2Pace += random.random()
                wynik += 1
                pygame.mixer.Sound.play(drink)
                promil += 0.1
        if abs(y - objy2) < 15:
            if abs(objx2 - x) < 15:
                kroky = -4
                y2Pace += random.random()
                objy2 = random.randint(-60, -20)
                objx2 = random.randint(10, 490)
                wynik += 1
                pygame.mixer.Sound.play(drink)
                promil += 0.1

        if wynik >= 5:
            y1Pace = 6
        if wynik >= 10:
            y2Pace = 6

        if objy > 520:
            promil -= 1
            if promil <= 0:
                pygame.mixer.Sound.play(lost)
                x = 300
                y = 490
                objx = random.randint(10, 490)
                objy = random.randint(-60, -20)
                objx1 = random.randint(10, 490)
                objy1 = random.randint(-60, -20)
                objx2 = random.randint(10, 490)
                objy2 = random.randint(-60, -20)
                szer = 10
                wys = 10
                krok = 10
                kroky = 0
                gamePace = 3
                yPace = 3
                y1Pace = 0
                y2Pace = 0
                promil = 0.1
                gameLost = True
            else:
                pygame.mixer.Sound.play(lost_beer)
                objy = random.randint(-60, -20)

        if objy1 > 520:
            promil -= 1
            if promil <= 0:
                pygame.mixer.Sound.play(lost)
                x = 300
                y = 490
                objx = random.randint(10, 490)
                objy = random.randint(-60, -20)
                objx1 = random.randint(10, 490)
                objy1 = random.randint(-60, -20)
                objx2 = random.randint(10, 490)
                objy2 = random.randint(-60, -20)
                szer = 10
                wys = 10
                krok = 10
                kroky = 0
                gamePace = 3
                yPace = 3
                y1Pace = 0
                y2Pace = 0
                promil = 0.1
                gameLost = True
            else:
                pygame.mixer.Sound.play(lost_beer)
                objy1 = random.randint(-60, -20)

        if objy2 > 520:
            promil -= 1
            if promil <= 0:
                pygame.mixer.Sound.play(lost)
                x = 300
                y = 490
                objx = random.randint(10, 490)
                objy = random.randint(-60, -20)
                objx1 = random.randint(10, 490)
                objy1 = random.randint(-60, -20)
                objx2 = random.randint(10, 490)
                objy2 = random.randint(-60, -20)
                szer = 10
                wys = 10
                krok = 10
                kroky = 0
                gamePace = 3
                yPace = 3
                y1Pace = 0
                y2Pace = 0
                promil = 0.1
                gameLost = True
            else:
                pygame.mixer.Sound.play(lost_beer)
                objy2 = random.randint(-60, -20)

        pygame.draw.rect(win, red, (x, y, szer, wys))
        pygame.draw.rect(win, green, (objx, objy, szer, wys))
        pygame.draw.rect(win, green, (objx1, objy1, szer, wys))
        pygame.draw.rect(win, green, (objx2, objy2, szer, wys))
        pygame.draw.line(win, (0, 0, 0), (0, 500), (500, 500), 5)
        win.blit(beer, (objx-5, objy-5))
        win.blit(beer1, (objx1 - 5, objy1 - 5))
        win.blit(beer2, (objx2 - 5, objy2 - 5))
        win.blit(character, (x-10, y-10))
    pygame.display.update()

pygame.quit()
