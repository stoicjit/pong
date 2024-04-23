from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# game components
ball = Ball()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

scoreboard = Scoreboard()

# movements
screen.listen()
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # wall bounce
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    # paddle bounce
    if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
        if ball.xcor() > 320 or ball.xcor() < -320:
            ball.bounce_x()
    # r_paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.point_l()

    # l_paddle misses
    if ball.xcor() < - 380:
        ball.reset()
        scoreboard.point_r()

screen.exitonclick()
