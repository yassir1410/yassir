from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
#setup the screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")

# screen.tracer(0) # create the paddles without seeing the moving
paddler=Paddle(350, 0)
paddlef=Paddle(-350,0)
screen.update()  #see the paddles

ball=Ball(paddler,paddlef)

# screen.tracer(1)
screen.listen()
screen.onkey(fun=paddler.up,key="Up")
screen.onkey(fun=paddler.down,key="Down")
screen.onkey(fun=paddlef.up,key="a")
screen.onkey(fun=paddlef.down,key="w")
# screen.onkey(fun=ball.move,key="m")
game_on=True
while game_on:
    ball.move()
    time.sleep(0.1)
    screen.update()


    ball.tracker.append(ball.xcor())
    

    if ball.wall_collosion():
        break
        # game_on=False

screen.update()
# time.sleep(0.1)

while not ball.is_down() and not ball.is_right_pad() and not ball.is_left_pad() and (ball.xcor()<400 and ball.xcor()>(-400)):
    ball.upper_coll()
    print("ball cor",ball.xcor(), ball.ycor())
    print("paddler",paddler.minp(),paddler.maxp())
    print(paddler.xcor())
    if ball.is_right_pad():
        print("hello worldddddddddddddddddddddddddddddd")
        for i in range(5):
            ball.r_pad_col()
            time.sleep(1)
            screen.update()
    time.sleep(1)
    screen.update()
    # if ball.right_pad():
    #     print("hello world")
print(ball.xcor(),ball.ycor())
ball.ycor()
    # elif ball.is_down():
    #     ball.lower_coll()
    # elif ball.right_pad():
    #     ball.r_pad_col()
    # elif ball.left_pad():
    #     ball.l_pad_col()







    

screen.exitonclick()