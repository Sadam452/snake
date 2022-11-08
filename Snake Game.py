# This project is a small snake game where user can move the snake left, right, up & down to eat food and score
import turtle
import time
import random
 
delay = 0.5
score = 0
high_score = 0

# Creating a screen to show output
wn = turtle.Screen()
wn.title("Snake - Project | Designed and developed by @Sadam452")
wn.bgcolor("grey")
 
# setting height and width
wn.setup(width=800, height=700)
wn.tracer(0)
 
 
# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
 
# What to eat
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)
 
rules= turtle.Turtle()
rules.speed(0)
rules.shape("square")
rules.color("white")
rules.penup()
rules.hideturtle()
rules.goto(-150,+270)
rules.write("Rule 1: Press 'u', 'r', 'd', 'l' to move up, right, down , left respectively.\n"
"Rule 2: Eat the 'Blue Circle food' to score.\n"
"Rule 3: Eating one food grain adds 10 to your score.\n"
"Rule 4: Going close to boundaries will end your game.", align="center",
          font=("Times New Roman", 11, "bold"))


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Highest Score : 0 | Current Score : 0", align="center",
          font=("Times New Roman", 20, "bold"))


# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(goup, "u")
wn.onkeypress(godown, "d")
wn.onkeypress(goleft, "l")
wn.onkeypress(goright, "r")

segments = []
 
# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 230 or head.ycor() < -320:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = 'blue';
        shapes = 'circle';
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.5
        pen.clear()
        pen.write("Highest Score : {} | Current Score : {} ".format(
            high_score,score), align="center", font=("Times New Roman", 20, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-370, 370)
        y = random.randint(-300, 230)
        food.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Highest Score : {} | Current Score : {} ".format(
            high_score,score), align="center", font=("Times New Roman", 20, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = 'blue';
            shapes = 'circle';
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.5
            pen.clear()
            pen.write("Highest Score : {} | Current Score : {} ".format(
                high_score, score), align="center", font=("Times New Roman", 20, "bold"))
    time.sleep(delay)
 
wn.mainloop()