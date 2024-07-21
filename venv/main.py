from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# setup the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
# screen.tracer(0) # create the paddles without seeing the moving
paddler = Paddle(350, 0)
paddlef = Paddle(-350, 0)
# screen.update()  # see the paddles

ball = Ball(paddler, paddlef)
screen.listen()

screen.onkey(fun=paddler.up, key="Up")
screen.onkey(fun=paddler.down, key="Down")
screen.onkey(fun=paddlef.up, key="a")
screen.onkey(fun=paddlef.down, key="w")

l = []
for i in range(20):
    turtle = Turtle()
    turtle.penup()
    turtle.setx(0)
    turtle.sety(300 - 30 * i)
    turtle.shape("square")
    turtle.color("white")
    turtle.shapesize(1, 0.5)
    l.append(turtle.ycor())

# screen.tracer(1)
scoreboard = Scoreboard()
scoreboard.showscore1()
scoreboard.showscore2()
screen.update()
# screen.onkey(fun=ball.move,key="m")
def initilizer(ball):
    # global scoreboard


    while not ball.wall_collosion():
        screen.update()
        time.sleep(0.04)
        ball.move()


def Game(ball):
    initilizer(ball)

    cond1 = ball.is_right_pad
    cond2 = ball.is_down
    cond3 = ball.is_left_pad
    action1 = ball.r_pad_col
    action2 = ball.lower_coll
    action3 = ball.l_pad_col

    current_action = ball.upper_coll
    current_stat = ball.is_up
    while (not cond1()) and (not cond2()) and (not cond3()):
        screen.update()
        # time.sleep(0.04)
        ball.tracker_x.append(ball.xcor())
        ball.tracker_y.append(ball.ycor())
        current_action()
        if cond1() or cond2() or cond3():
            if cond1():
                current_stat, cond1 = cond1, current_stat


                current_action,action1=action1,current_action
            elif cond2():
                current_stat, cond2 = cond2, current_stat

                current_action,action2=action2,current_action
            elif cond3():
                current_stat, cond3 = cond3, current_stat

                current_action,action3=action3,current_action
        if ball.xcor()<=-400 or ball.xcor()>=400:
            ball.tracker_x=[0]
            ball.tracker_y=[0]
            break
def update_score(scoreboard):
    if ball.xcor()<=-400:
        scoreboard.increment1()
        scoreboard.clear()
    else:
        scoreboard.increment2()
        scoreboard.clear()
    scoreboard.showscore1()
    scoreboard.showscore2()





game_on=True
while game_on:
    Game(ball)
    # screen.tracer(0)
    update_score(scoreboard)
    ball.goto(0,0)
    screen.update()

screen.exitonclick():

