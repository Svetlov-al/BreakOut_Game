from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self, hitter):
        super().__init__()
        self.color('coral')
        self.penup()
        self.hideturtle()
        self.point = 000
        self.hitter = hitter
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.pad_left = len(self.hitter.all_paddles)
        self.write(str(self.point).zfill(3), align='center',
                   font=("Arial", 60, "normal"))
        self.goto(100, 250)
        self.write(str(self.pad_left).zfill(3), align='center',
                   font=("Arial", 60, "normal"))
        
        
    def pointer(self):
        self.point += 1
        self.update_score()
    
    def pad_lefter(self):
        self.pad_left -= 1
        self.update_score()
        
    def game_is_over(self):
        self.color('AliceBlue')
        self.goto(0, 0)
        self.write("GAME IS OVER", align='center', font=FONT)