from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color('cyan')
        self.shape('square')
        self.shapesize(stretch_wid=0.7, stretch_len=4)
        self.penup()
        self.goto(position)
        
    
    def left(self):
        if self.xcor() >= -250:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())
    
    def right(self):
        if self.xcor() < 250:
            new_x = self.xcor() + 10
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())
