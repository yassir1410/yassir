from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score1=0
        self.score2=0
        self.speed(0)
        self.penup()
        self.color("white")
    def showscore1(self):
        self.sety(190)
        self.setx(50)
        self.write(arg=f"{self.score1}",align="center",move=False,font=('Arial', 80, 'normal'))
    def showscore2(self):    
        self.sety(190)
        self.setx(-50)
        self.write(arg=f"{self.score2}",align="center",move=False,font=('Arial', 80, 'normal'))
    def game_over(self):
        self.sety(0)
        self.color("white")
        self.write(arg="Game Over", align="center", move=False, font=('Arial', 50, 'normal'))
        
    def increment2(self):
        self.score2+=1
        print(f"this is score2:{self.score2}")
    def increment1(self):
        self.score1+=1
        print(f"this is score2:{self.score1}")