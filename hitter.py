from turtle import Turtle

COLORS = ["red", "red", "yellow", "yellow", "blue", "blue"]

class Hitter(Turtle):
    def __init__(self):
        self.all_paddles = []
        
        
    def create_puddles(self):
        
        place_y = 200
        for color in COLORS:
            place_x = -250
            for pad in range(11):
                pad = Turtle("square")
                pad.color(color)
                pad.shapesize(stretch_wid=0.5, stretch_len=2)
                pad.penup()
                pad.goto(place_x, place_y)
                place_x += 50
                self.all_paddles.append(pad)
            place_y -= 20