from turtle import Turtle
from paddle import Paddle
class Ball(Turtle):
    def __init__(self, paddler: "Paddle",paddlef:"Paddle"):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.setposition(0,0)
        self.speed("slowest")
        self.tracker_x=[0]
        self.tracker_y=[0]
        self.penup()
        self.paddler=paddler
        self.paddlef=paddlef
    def move(self):
        new_x=self.xcor()+10
        new_y=self.ycor()+10
        self.goto(new_x,new_y)
    def wall_collosion(self):
        if self.ycor()==290 or self.ycor()<=-290:
            return True
    def is_up(self):
        return self.ycor()==290
    def is_down(self):
        return self.ycor()==-290

    def upper_coll(self):
        if self.tracker_x[-1]>self.tracker_x[-2]:
                new_x = self.xcor() +10
                new_y = self.ycor()-10
                self.goto(new_x, new_y)
        else:
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)

    def lower_coll(self):
        if self.tracker_x[-1] < self.tracker_x[-2]:
            new_x = self.xcor() - 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
        else:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
    def r_pad_col(self):
        if self.tracker_y[-1] > self.tracker_y[-2]:
            new_x = self.xcor() - 10
            new_y = self.ycor() -10
            self.goto(new_x, new_y)
        else:
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)
    def l_pad_col(self):
        if self.tracker_y[-1] < self.tracker_y[-2]:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
        else:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
    def is_right_pad(self):
        if self.paddler.minp()<=self.ycor()<=self.paddler.maxp() and self.paddler.xcor()-20==self.xcor():
            return True
    def is_left_pad(self):
        if self.paddlef.minp()<= self.ycor()<=self.paddlef.maxp() and self.paddlef.xcor()+20==self.xcor():
            return True
        
        
        
