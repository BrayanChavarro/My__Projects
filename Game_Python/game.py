import turtle
#WindoW
wdow= turtle.Screen()
wdow.title("Ping Pong Xtreme")
wdow.bgcolor("green")
wdow.setup(width=800, height=600)
wdow.tracer(0)

#Point marker

Point_markerA = 0
Point_markerB = 0

#PlayerA

PlayerA=turtle.Turtle()
PlayerA.speed(0)
PlayerA.shape("square")
PlayerA.color("white")
PlayerA.penup()
PlayerA.goto(-350,0)
PlayerA.shapesize(stretch_wid=5, stretch_len=1)

#PLayerB

PlayerB=turtle.Turtle()
PlayerB.speed(0)
PlayerB.shape("square")
PlayerB.color("white")
PlayerB.penup()
PlayerB.goto(350,0)
PlayerB.shapesize(stretch_wid=5, stretch_len=1)

#Ball

Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)

#Modyfy these variables to change ball velocity

Ball.dx = 0.8
Ball.dy = 0.8

#Division Line

Division=turtle.Turtle()
Division.color("white")
Division.goto(0,400)
Division.goto(0,-400)

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("courier", 24, "normal"))

#Funtions

def JA_up():
    y=PlayerA.ycor()
    y += 20
    PlayerA.sety(y)

def JA_down():
    y=PlayerA.ycor()
    y -= 20
    PlayerA.sety(y)   

def JB_up():
    y=PlayerB.ycor()
    y += 20
    PlayerB.sety(y)

def JB_down():
    y=PlayerB.ycor()
    y -= 20
    PlayerB.sety(y)   

#Keyboard

wdow.listen()
wdow.onkeypress(JA_up, "w")
wdow.onkeypress(JA_down, "s")
wdow.onkeypress(JB_up, "Up")
wdow.onkeypress(JB_down, "Down")

while True:
    wdow.update()

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Checks for collisions with window edges
    if Ball.ycor() > 290:
        Ball.dy *= -1
    if Ball.ycor() < -290:
        Ball.dy *= -1
    
    # If the ball goes out to the left or right, it returns to the center.
    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        Point_markerA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Point_markerA,Point_markerB), align="center", font=("courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        Point_markerB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Point_markerA,Point_markerB), align="center", font=("courier", 24, "normal"))

    if ((Ball.xcor() > 340 and Ball.xcor() < 350)
            and (Ball.ycor() < PlayerB.ycor() +50 and Ball.ycor() > PlayerB.ycor() -50)):
            Ball.dx *= -1
            Ball.dy *= -1
            
    if ((Ball.xcor() < -340 and Ball.xcor() > -350)
            and (Ball.ycor() < PlayerA.ycor() +50 and Ball.ycor() > PlayerA.ycor() -50)):
            Ball.dx *= -1
            Ball.dy *= -1
