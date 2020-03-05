#Pong Game for Python3 

import turtle 
import winsound

wn = turtle.Screen() 
wn.title("Pong")
wn.bgcolor("black") 
wn.setup(width=800, height = 600) 
wn.tracer(0) 

# Scoreboard  
pen = turtle.Turtle() 
pen.speed(0) 
pen.color("white")
pen.penup() 
pen. hideturtle() 
pen.goto(0,260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24,"normal"))

#Score 
score1 = 0 
score2 = 0

#Player 1 Paddle 
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350, 0) 

#Player 2 Paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0) 

#Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = .25 
ball.dy = .25

# Functions
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)
    
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)
    
def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
# Key bindings
wn.listen()
wn.onkeypress(paddle1_up,"w")
wn.onkeypress(paddle1_down,"s")
wn.onkeypress(paddle2_up,"Up")
wn.onkeypress(paddle2_down,"Down")

#Main game loop
while True: 
    wn.update()
    
    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border check
    
    if ball.ycor() > 290: #top border
       ball.sety(290)
       ball.dy *= -1
       winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290: #bottom border
       ball.sety(-290)
       ball.dy *= -1 
       winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
       
       
    if ball.xcor() > 390:#right border
       ball.goto(0,0)
       ball.dx *= -1
       #ball.dx -=2
       #ball.dy -=2
       score1 += 1
       pen.clear()
       pen.write("Player 1: {} Player 2: {}".format (score1, score2), align="center", font=("Courier", 24,"normal"))

    
    if ball.xcor() < -390:#left border
       ball.goto(0,0)
       ball.dx *= -1
       #ball.dx -= 2
       #ball.dy -= 2
       score2 += 1
       pen.clear() 
       pen.write("Player 1: {} Player 2: {}".format (score1, score2), align="center", font=("Courier", 24,"normal"))


    #Ball collisions 
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 
    and ball.ycor() > paddle2.ycor() - 40): #Paddle 2 Collison
         ball.setx(340)
         ball.dx *= -1
         #ball.dx +=.5
         #ball.dy +=.5
         winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 
    and ball.ycor() > paddle1.ycor() - 40): #Paddle 1 Collision
         ball.setx(-340)
         ball.dx *= -1
         #ball.dx +=.5
         #ball.dy +=.5
         winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
         