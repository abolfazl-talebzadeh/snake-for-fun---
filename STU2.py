import pygame, random


def s_ini():
    snake.append([random.randint(1, 40) * 10, random.randint(1, 49) * 10, 0])
    snake.append([snake[0][0] - 10, snake[0][1], 0])
    snake.append([snake[1][0] - 10, snake[1][1], 0])
    snake.append([snake[2][0] - 10, snake[2][1], 0])
    snake.append([snake[3][0] - 10, snake[3][1], 0])
    snake.append([snake[4][0] - 10, snake[4][1], 0])
    snake.append([snake[5][0] - 10, snake[5][1], 0])


def transpass(s_r):
    if s_r[0][0] >= 500 or s_r[0][0] < 0:
        # print('side borders crossed', s_r)
        return True
    elif s_r[0][1] >= 500 or s_r[0][1] < 0:
        # print('Horizental borders crossed',s_r)
        return True
    for x in range(len(s_r) - 1):
        if s_r[0][0] == s_r[x + 1][0] and s_r[0][1] == s_r[x + 1][1]:
            print("Self crossed")
            return True


def add_child():
    lastsq = len(snake) - 1
    # print(snake, snake[lastsq])
    if snake[lastsq][2] == 0:
        snake.append([snake[lastsq][0] - 10, snake[lastsq][1], 0])
    elif snake[lastsq][2] == 1:
        snake.append([snake[lastsq][0], snake[lastsq][1] - 10, 1])
    elif snake[lastsq][2] == 2:
        snake.append([snake[lastsq][0] + 10, snake[lastsq][1], 2])
    elif snake[lastsq][2] == 3:
        snake.append([snake[lastsq][0], snake[lastsq][1] + 10, 3])


def add_target():
    target[0] = random.randint(1, 40) * 10
    target[1] = random.randint(1, 49) * 10



snake = []
target = [0, 0]
direction = 0
s_ini()
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Iliya Game!")
x = 5
y = 5
width = 5
height = 5
vel = 5
run_mode = True
add_target()
while run_mode:
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_mode = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if direction != 0:
            direction = 2
            snake[0][2] = 2

    if keys[pygame.K_RIGHT]:
        if direction != 2:
            direction = 0
            snake[0][2] = 0

    if keys[pygame.K_UP]:
        if direction != 1:
            direction = 3
            snake[0][2] = 3
    if keys[pygame.K_DOWN]:
        if direction != 3:
            direction = 1
            snake[0][2] = 1

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (155, 13, 56), (target[0], target[1], 10, 10))
    for xx in range(int(len(snake))):
        pygame.draw.rect(win, (255, 23, 56), (snake[xx][0], snake[xx][1], 10, 10))
        pygame.display.update()

    # ////transpass check
    if transpass(snake):
        pygame.quit()
        break

    for xx in range(int(len(snake))):
        if snake[xx][2] == 0:
            snake[xx][0] += 10
        elif snake[xx][2] == 1:
            snake[xx][1] += 10
        elif snake[xx][2] == 2:
            snake[xx][0] -= 10
        elif snake[xx][2] == 3:
            snake[xx][1] -= 10

    if abs(snake[0][0] - target[0]) < 5 and abs(snake[0][1] - target[1]) < 5:
        add_target()
        add_child()
    elif abs(snake[0][0] - target[0]) < 5 and abs(snake[0][1] - target[1]) < 5:
        add_target()
        add_child()

    for xx in range(int(len(snake))):
        if xx != 0:
            snake[len(snake) - xx][2] = snake[len(snake) - xx - 1][2]
        snake[0][2] = direction
