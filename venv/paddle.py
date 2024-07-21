from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xc,yc):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        # self.xc=xc
        # self.yc=yc
        self.setposition(xc,yc)
        self.current_pos=self.ycor()
        # self.maxp=self.ycor()+2.5
        # self.minp=self.ycor()-2.5
    def up(self):
        self.current_pos+=20
        self.sety(self.current_pos)
    def down(self):
        self.current_pos -= 20
        self.sety(self.current_pos)
    def get_pos(self):
        return self.ycor()
    def maxp(self):
        return self.ycor()+50
    def minp(self):
        return self.ycor()-50
    
