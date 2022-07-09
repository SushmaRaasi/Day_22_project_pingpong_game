from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

"""
paddle = Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(380, 0)
"""

screen.listen()

"""
def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

"""

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()
