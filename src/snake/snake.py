from random import randrange
from time import sleep
from turtle import *

from gamebase import square

snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
apple_x = randrange(-19, 18) * 10
apple_y = randrange(-19, 18) * 10
aim_x = 10
aim_y = 0


def wall(x: int, y: int) -> int:
    if x > 180:
        x = -190
    elif x < -190:
        x = 190
    if y > 180:
        y = -190
    elif y < -190:
        y = 190
    return x, y


def change(x: int, y: int):
    global aim_x, aim_y
    aim_x = x
    aim_y = y


def inside():
    head = snake[-1]
    return head in snake[:-1]


def gameLoop():
    global apple_x, apple_y, snake, aim_x, aim_y

    head_x = snake[-1][0] + aim_x
    head_y = snake[-1][1] + aim_y
    head_x, head_y = wall(
        head_x, head_y
    )  # 只需要对蛇头判断穿墙就可以了,因为这个蛇头就是下一秒的蛇身

    snake.append([head_x, head_y])  # 移动

    if (
        snake[-1][0] == apple_x and snake[-1][1] == apple_y
    ):  # 吃苹果的判断与新苹果的生成
        while [apple_x, apple_y] in snake:
            apple_x = randrange(-19, 18) * 10
            apple_y = randrange(-19, 18) * 10
    else:
        snake.pop(0)

    if inside():  # 判断是否死亡
        square(snake[-1][0], snake[-1][1], 10, 'red')
        update()
        sleep(2)
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
        apple_x = randrange(-19, 18) * 10
        apple_y = randrange(-19, 18) * 10
        aim_x = 10
        aim_y = 0

    clear()
    # 绘制黑色边框（边框宽度为10像素）
    square(-200, -200, 400, 'black')
    square(-190, -190, 380, 'white')

    square(apple_x, apple_y, 10, 'red')  # 绘画苹果

    for i in range(len(snake)):  # 绘画snake
        square(snake[i][0], snake[i][1], 10, 'black')

    ontimer(gameLoop, 150)
    update()


setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(10, 0), 'd')
gameLoop()
done()
