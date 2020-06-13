import pygame
import random
import math

pygame.init()

body = []
white = 255, 255, 255
x = 500  # x pos of snake
y = 350  # y pos of snake
x_move = 0
y_move = 0
snake_speed = 7  # speed of snake
apple_x = random.randrange(40, 700)  # will get rondom x pos of apple
apple_y = random.randrange(40, 1000)  # will get rondom y pos of apple
snake_length = 2  # length of snake
flag = 0
score = 0
size = width, height = 1000, 700
screen = pygame.display.set_mode((size))

# draws the head of snake
def snake_head(x, y):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 20, 20))


# draws the body of snake
def snake():
    for i in body:
        pygame.draw.rect(screen, (0, 255, 0), [i[0], i[1], 20, 20])


# draws the apple
def apple(x2, y2):
    pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 20, 20))


# get formula for collision
def eat():
    d = math.sqrt((x - apple_x) ** 2 + (y - apple_y) ** 2)
    if d < 20:
        return True
    else:
        return False


# displays text
def text(msg, txtX, txtY):
    style = pygame.font.SysFont('comicsansms', 50)
    screen.blit(style.render(msg, True, (50, 200, 30)), (txtX, txtY))


clock = pygame.time.Clock()

run = True
# main game loop
while run:
    for event in pygame.event.get():
        # checks weather exit button is clicked
        if event.type == pygame.QUIT:
            run = False

        # checks for event keys (left,right,down,up)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and flag == 1:
                x_move -= 20
                y_move = 0
                flag = 0

            elif event.key == pygame.K_RIGHT and flag == 1:
                x_move += 20
                y_move = 0
                flag = 0

            elif event.key == pygame.K_DOWN and flag == 0:
                y_move += 20
                x_move = 0
                flag = 1

            elif event.key == pygame.K_UP and flag == 0:
                y_move -= 20
                x_move = 0
                flag = 1

    # increases accordingly to last key pressed
    y += y_move
    x += x_move
    lst = []
    lst.append(x)
    lst.append(y)
    # gets last x and y position of the snake and increases length
    body.append(lst)

    if len(body) > snake_length:
        body.pop(0)

    # checks if snake is out of boundary
    if y < 40 or y > 700 or x < 0 or x > 1000:
        run = False

    screen.fill(white)
    pygame.draw.rect(screen, (0, 250, 250), (0, 0, 1000, 40))
    text("Score: " + str(score), 10, 10)
    snake()
    snake_head(x, y)
    apple(apple_x, apple_y)
    pygame.display.update()

    # checks weather the snakes head is collided with the apple
    ate = eat()
    if ate:
        apple_x = random.randrange(40, 500)  # resets the x pos of apple
        apple_y = random.randrange(40, 500)  # resets the x pos of apple
        snake_length += 1  # increases length of snake
        score += 100  # increases score by 100
        snake_speed += 0.5  # increases speed
    clock.tick(snake_speed)
