# Import modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating display for the game
display = turtle.Screen()
display.title("Snake Game")
display.bgpic('Snake_Game_Background.png')

# Set height and width of the display
display.setup(width=600, height=600)
display.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
colors = random.choice(['red', 'blue'])
shapes = random.choice(['square', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Scoreboard
score_board = turtle.Turtle()
score_board.speed(0)
score_board.shape("square")
score_board.color("black")
score_board.hideturtle()
score_board.goto(0, 250)
score_board.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

# Assign keys to play

# Defining methods to go which directions
def goUp(): 
    if head.direction != "down":
        head.direction = "up"

def goDown(): 
    if head.direction != "up":
        head.direction = "down"

def goLeft(): 
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

# Define method move to move the snake based on the direction that has been chosen 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Assign key buttons to the directions
display.listen()
display.onkeypress(goUp, "w")
display.onkeypress(goDown, "s")
display.onkeypress(goLeft, "a")
display.onkeypress(goRight, "d")

# Main gameplay

segments = []

while True:
    display.update()
    # If snake went out of bounds, reset the game
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'triangle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        score_board.clear()
        score_board.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

    # Adding segments
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("white")
    new_segment.penup()
    segments.append(new_segment)
    score += 10
    if score > high_score:
            high_score = score
    score_board.clear()
    score_board.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    # Check to see if we have head collision with the body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
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
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'triangle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            score_board.clear()
            score_board.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
display.mainloop()