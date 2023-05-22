from turtle import Screen
from paddle import Paddle
from hitter import Hitter
from ball import Ball
from scoreboard import ScoreBoard
# -------------------

paddle = Paddle((0, -280))

# -------------------

hitter = Hitter()

#--------------------

ball = Ball()

#--------------------

score = ScoreBoard(hitter)

#--------------------
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 700)
screen.title("BreakOut Game")
screen.listen()
screen.tracer(0)


screen.onkeypress(paddle.left, 'Left')
screen.onkeypress(paddle.right,'Right')

game_is_on = True

def update():
    global game_is_on
    if game_is_on:
        screen.update()
        screen.ontimer(update, 50)
        ball.move()
        if ball.xcor() == 280 or ball.xcor() == -280:
            ball.bounce_x()
        if ball.ycor() > 280:
            ball.bounce_y()
        elif ball.ycor() < -350:
            ball.reset_position()
            score.game_is_over()
            game_is_on = False
        if ball.distance(paddle) < 25:
            ball.bounce_y()
        for hit in hitter.all_paddles:
            if hit.distance(ball) < 30:
                hit.hideturtle()
                hitter.all_paddles.remove(hit)
                ball.bounce_y()
                score.pointer()


update()
hitter.create_puddles()
score.update_score()
screen.mainloop()    

