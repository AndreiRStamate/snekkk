import pygame
import random
import time

def pause():
    paused = True

    gameDisplay.fill(white)
    message_to_center("Game paused", black, -100, "large")
    message_to_center("Press 'p' to unpause or q to quit.", black, 25)
    pygame.display.update()
    clock.tick(5)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


def randAppleGen():
    randAppleX = round(random.randrange(0, width - applethikness))
    randAppleY = round(random.randrange(0, height - applethikness))

    return randAppleX, randAppleY


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_v:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_center("Welcome to my game", green, -200, 'large')
        message_to_center("Eat the red apples and dont crash into yourself", black, -110)
        message_to_center("Eat them all", black, -70)
        message_to_center("C to play, p to pause, q to quit", black, 20)
        pygame.display.update()
        clock.tick(24)


def text_objects(text, c, size):
    if size == "small":
        textsurface = smallfont.render(text, True, c)
    elif size == "medium":
        textsurface = medfont.render(text, True, c)
    elif size == "large":
        textsurface = largefont.render(text, True, c)

    return textsurface, textsurface.get_rect()


def message_to_center(msg, c, y_displace=0, size="small"):
    textsurf, textrect = text_objects(msg, c, size)
    textrect.center = (width / 2), (height / 2) + y_displace
    gameDisplay.blit(textsurf, textrect)


def message_to_corner(msg, c):
    screen_text = smallfont.render(msg, True, c)
    gameDisplay.blit(screen_text, [5, 1])


def message_to_corner2(msg, c):
    screen_text = smallfont.render(msg, True, c)
    gameDisplay.blit(screen_text, [width-150, 1])


def snake(block_s, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(snekimg, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snekimg, 90)
    if direction == 'up':
        head = snekimg
    if direction == 'down':
        head = pygame.transform.rotate(snekimg, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-5]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_s, block_s])


def snake2(block_s, snakelist):
    if direction2 == 'right':
        head = pygame.transform.rotate(snek2img, 270)
    if direction2 == 'left':
        head = pygame.transform.rotate(snek2img, 90)
    if direction2 == 'up':
        head = snek2img
    if direction2 == 'down':
        head = pygame.transform.rotate(snek2img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-5]:
        pygame.draw.rect(gameDisplay, blue, [XnY[0], XnY[1], block_s, block_s])


pygame.init()

icon = pygame.image.load('icon.png')
snekimg = pygame.image.load('snakeHead.png')
snek2img = pygame.image.load('snake2Head.png')
appleimg = pygame.image.load('apple.png')

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 30)
largefont = pygame.font.SysFont("comicsansms", 40)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 205, 0)
blue = (0, 162, 232)

fps = 60

direction = 'up'
direction2 = 'up'

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
speed = 4
speed2 = 4
block_size = 20
applethikness = 30

clock = pygame.time.Clock()

pygame.display.set_caption(r"Slytherino.exe")
pygame.display.set_icon(icon)
pygame.display.update()


def gameloop(mode_set):

    while mode_set is False:
        mode_crash = False
        mode_points = False
        gameDisplay.fill(white)
        message_to_center("X for crash, V for points", black)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    mode_crash = True
                    mode_set = True
                    break
                elif event.key == pygame.K_v:
                    mode_points = True
                    mode_set = True
                    break
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    global direction
    global direction2
    global speed
    global speed2
    lead_x = 400
    lead_y = 300
    lead_x2 = 500
    lead_y2 = 400
    lead_x_change = 0
    lead_y_change = 0
    lead_x2_change = 0
    lead_y2_change = 0
    points = 0
    points2 = 0
    point = 1
    point2 = 1
    player1crashed = False
    player2crashed = False
    s = 0
    s2 = 0
    p = 0
    p2 = 0
    cd = 0
    cd2 = 0
    dc = 0
    dc2 = 0
    cooldown = False
    cooldown2 = False
    cooldown_speed = False
    cooldown_speed2 = False

    randAppleX, randAppleY = randAppleGen()

    snakelist = []
    snakelist2 = []
    snakelength = 1
    snakelength2 = 1

    gamedone = False
    done = True
    gameover = False

    while gamedone is not done:

        while gameover:
            gameDisplay.fill(white)
            message_to_center("Game over", red, y_displace=-40, size='large')
            message_to_center("Press c to play again or q to quit", black, y_displace=20, size='medium')

            text = "The green snek ate 50 apples first, the best apple eater in the world"
            text2 = "The blue snek ate 50 apples first, the best apple eater in the world"

            if points >= 50:
                message_to_center(text, green, y_displace=60)
            if points2 >= 50:
                message_to_center(text2, blue, y_displace=60)

            if player1crashed:
                message_to_center("Mr Blue WON!!!", blue, y_displace=80)
            if player2crashed:
                message_to_center("Mr Green WON!!!", green, y_displace=80)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop(f)
                    if event.key == pygame.K_q:
                        gameover = False
                        gamedone = True
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamedone = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    gamedone = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change = -speed
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change = speed
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -speed
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = speed
                    direction = "down"
                elif event.key == pygame.K_a:
                    lead_y2_change = 0
                    lead_x2_change = -speed2
                    direction2 = 'left'
                elif event.key == pygame.K_d:
                    lead_y2_change = 0
                    lead_x2_change = speed2
                    direction2 = 'right'
                elif event.key == pygame.K_w:
                    lead_x2_change = 0
                    lead_y2_change = -speed2
                    direction2 = 'up'
                elif event.key == pygame.K_s:
                    lead_x2_change = 0
                    lead_y2_change = speed2
                    direction2 = 'down'
                elif event.key == pygame.K_KP0:
                    if cooldown_speed is False: #and mode_crash is False:
                        speed = 6
                        cooldown_speed = True
                elif event.key == pygame.K_f:
                    if cooldown_speed2 is False:
                        speed2 = 6
                        cooldown_speed2 = True
                elif event.key == pygame.K_KP1:
                    if cooldown is False:
                        point = 3
                        cooldown = True
                elif event.key == pygame.K_r:
                    if cooldown2 is False:
                        point2 = 3
                        cooldown2 = True
                elif event.key == pygame.K_p:
                    pause()

        lead_x += lead_x_change
        lead_y += lead_y_change

        lead_x2 += lead_x2_change
        lead_y2 += lead_y2_change

        lead_x %= width
        lead_y %= height

        lead_x2 %= width
        lead_y2 %= height

        snakehead = [lead_x, lead_y]
        snakelist.append(snakehead)

        snakehead2 = [lead_x2, lead_y2]
        snakelist2.append(snakehead2)

        gameDisplay.fill(white)
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        if len(snakelist) > snakelength:
            del snakelist[0]
        if len(snakelist2) > snakelength2:
            del snakelist2[0]

        snake(block_size, snakelist)
        snake2(block_size, snakelist2)
        pygame.display.update()

        if mode_crash:
            if snakehead in snakelist2[:-1]:
                player1crashed = True
                gameover = True

            if snakehead2 in snakelist[:-1]:
                player2crashed = True
                gameover = True

        if randAppleX < lead_x < randAppleX + applethikness or randAppleX < lead_x + block_size < randAppleX + applethikness:
            if randAppleY < lead_y < randAppleY + applethikness or randAppleY < lead_y + block_size < randAppleY + applethikness:
                randAppleX, randAppleY = randAppleGen()
                snakelength += 5
                points += point

        if randAppleX < lead_x2 < randAppleX + applethikness or randAppleX < lead_x2 + block_size < randAppleX + applethikness:
            if randAppleY < lead_y2 < randAppleY + applethikness or randAppleY < lead_y2 + block_size < randAppleY + applethikness:
                randAppleX, randAppleY = randAppleGen()
                snakelength2 += 5
                points2 += point2

            if points >= 50 or points2 >= 50:
                gameover = True

        if mode_points:
            if speed == 6:
                s += 1
            if s >= fps*5:
                speed = 4
                s = 0
                cooldown_speed = True

            if speed2 == 6:
                s2 += 1
            if s2 >= fps*5:
                speed2 = 4
                s2 = 0
                cooldown_speed2 = True

            if cooldown_speed:
                cd += 1
            if cd >= fps*15:
                cooldown_speed = False
                cd = 0

            if cooldown_speed2:
                cd2 += 1
            if cd2 >= fps*15:
                cooldown_speed2 = False
                cd2 = 0

        if point == 3:
            p += 1
        if p >= fps*5:
            point = 1
            p = 0
            cooldown = True

        if point2 == 3:
            p2 += 1
        if p2 >= fps*5:
            point2 = 1
            p2 = 0
            cooldown2 = True

        if cooldown:
            dc += 1
        if dc >= fps*15:
            cooldown = False
            dc = 0

        if cooldown2:
            dc2 += 1
        if dc2 >= fps*15:
            cooldown2 = False
            dc2 = 0

        message_to_corner("points: " + str(points), black)
        message_to_corner2("points: " + str(points2), black)
        pygame.display.update()

        clock.tick(fps)

    message_to_center("Developed by me", black, y_displace=0, size='small')
    pygame.display.update()
    time.sleep(0.35)
    pygame.quit()
    quit()

f = False
t = True
game_intro()
gameloop(f)
