
from turtle import Turtle,Screen
from paddle import Paddle

from ball import Ball
import time 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

r_paddle = Paddle((350,0))
                
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#detect collision with wall

    if ball.ycor() > 300 or ball.ycor() < -300:
    # need to bounce back
        ball.bounce_y()
        #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >340 or ball.distance(l_paddle) <50 and ball.xcor() < -340:

        ball.bounce_x()
    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

