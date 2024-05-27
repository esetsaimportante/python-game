import turtle
import math
import random

win = turtle.Screen()
turtle.bgcolor("yellow")
win.tracer(3)

mypen= turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for x in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle() 




player_one= turtle.Turtle()
player_one.color("red")
player_one.penup()

player_one.speed(0)
player_one.shape("triangle")
player_one.setposition(0,200)

player_two= turtle.Turtle()
player_two.color("blue")
player_two.penup()

player_two.speed(0)
player_two.shape("triangle")
player_two.setposition(150,200)


max_ball=5
ball=[]
for count in range(max_ball):
    ball.append(turtle.Turtle())
    ball[count].penup()
    ball[count].color("black")
    ball[count].shape("circle")
    ball[count].speed(0)
    ball[count].setposition(random.randint(-300,300),random.randint(-300,300))


max_ball2=2
ball2=[]
for count in range(max_ball2):
    ball2.append(turtle.Turtle())
    ball2[count].penup()
    ball2[count].color("green")
    ball2[count].shape("circle")
    ball2[count].speed(0)
    ball2[count].setposition(random.randint(-300,300),random.randint(-300,300))   
    
    
    


speed =  0.3
speed2 = 0.3


def more_right():
    player_one.left(30)
def more_left():
    player_one.right(30)
def increase():
    global speed 
    speed += 0.2
def dicrease():
    global speed 
    speed -= 0.2

def more_right2():
    player_two.left(30)
def more_left2():
    player_two.right(30)
def increase2():
    global speed2 
    speed2 += 0.2
def dicrease2():
    global speed2 
    speed2 -= 0.2
    
    
def isConsille(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20 :
        return True
    else :
        False
        
def isConsille2(t,t2):
    c = math.sqrt(math.pow(t.xcor()-t2.xcor(),2) + math.pow(t.ycor()-t2.ycor(),2))
    if c < 20 :
        return True
    else :
        False

def isConsille(t1,t2):
    a = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if a < 20 :
        return True
    else :
        False
        
def isConsille2(t,t2):
    b = math.sqrt(math.pow(t.xcor()-t2.xcor(),2) + math.pow(t.ycor()-t2.ycor(),2))
    if b < 20 :
        return True
    else :
        False


score1 =0
score2 =0
score = turtle.Turtle()
score.color("black")
score.goto(0,330)
to_win= 15

win.listen()
turtle.onkey(more_right,"Right")
turtle.onkey(more_left,"Left")
turtle.onkey(increase,"Up")
turtle.onkey(dicrease,"Down")

turtle.onkey(more_right2,"a")
turtle.onkey(more_left2,"d")
turtle.onkey(increase2,"w")
turtle.onkey(dicrease2,"s")




while True:
    player_one.forward(speed)
    player_two.forward(speed2)
    
    
    if player_one.xcor() <-300 or player_one.xcor( )> 300:
        player_one.right(180) 
        
           
    if player_one.ycor() <-300 or player_one.ycor( )> 300:
        player_one.right(180)   
    
    
    if player_two.xcor() <-300 or player_two.xcor( )> 300:
        player_two.right(180) 
        
           
    if player_two.ycor() <-300 or player_two.ycor( )> 300:
        player_two.right(180)   
    
    for count in range(max_ball):
        ball[count].forward(0.8)
    
        if ball[count].xcor() <-300 or ball[count].xcor( )> 300:
            ball[count].right(180) 
            
            
        if ball[count].ycor() <-300 or ball[count].ycor( )> 300:
            ball[count].right(180) 
        
        if isConsille (player_one,ball[count]):
            ball[count].setposition(random.randint(-300,300),random.randint(-300,300))
            ball[count].right(random.randint(0,360))
            score1 += 1
            score.clear()
            score.write("player1 : {}  player2 : {}".format(score1,score2) , align= "center", font= (" Courior",20, "normal"))  
            
            
            
        if isConsille2(player_two,ball[count]):
            ball[count].setposition(random.randint(-300,300),random.randint(-300,300))
            ball[count].right(random.randint(0,360))
            score2 += 1
            score.clear()
            score.write("player1 : {}  player2 : {}".format(score1,score2) , align= "center", font= (" Courior",20, "normal"))
            
            
    for count in range(max_ball2):
        ball2[count].forward(0.8)
    
        if ball2[count].xcor() <-300 or ball2[count].xcor( )> 300:
                ball2[count].right(180) 
                
                
        if ball2[count].ycor() <-300 or ball2[count].ycor( )> 300:
                ball2[count].right(180) 
            
        if isConsille (player_one,ball2[count]):
                ball2[count].setposition(random.randint(-300,300),random.randint(-300,300))
                ball2[count].right(random.randint(0,360))
                score1 -= 5
                score.clear()
                score.write("player1 : {}  player2 : {}".format(score1,score2) , align= "center", font= (" Courior",20, "normal"))  
                
                
                
        if isConsille2(player_two,ball2[count]):
                ball2[count].setposition(random.randint(-300,300),random.randint(-300,300))
                ball2[count].right(random.randint(0,360))
                score2 -= 5
                score.clear()
                score.write("player1 : {}  player2 : {}".format(score1,score2) , align= "center", font= (" Courior",20, "normal"))
                
        if score1 == to_win :
            player_one.clear
            player_two.clear
            ball.clear
            ball2.clear
            to_win.write("player one wins ", align= "center",font = (" Courior",36, "normal") )
            