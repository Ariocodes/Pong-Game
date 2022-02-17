import turtle
# import os
# Mac = os.system('afplay bounce.wav&')
# Linux = os.system('aplay bounce.wav&')
import winsound
wn = turtle.Screen()
wn.title('Pong game by Ario')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=7, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)
# Paddle right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=7, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # 1
ball.dy = 0.2 # 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A:0 Player B: 0', align='center', font=('Courier', 14, 'normal'))

# Function
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)
def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)
def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_left_up, 'w')
wn.onkeypress(paddle_left_down, 's')
wn.onkeypress(paddle_right_up, 'Up')
wn.onkeypress(paddle_right_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A:{} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 14, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A:{} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 14, 'normal'))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 70 and ball.ycor() > paddle_right.ycor() - 70):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 70 and ball.ycor() > paddle_left.ycor() - 70):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
