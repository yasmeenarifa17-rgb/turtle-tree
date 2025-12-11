import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.color("light pink")
t.left(90)
t.penup()
t.goto(0, -300)
t.pendown()

def draw_branch(length):
    if length < 5:
        return
    
    # Change color randomly for leaves
    if length < 20:
        t.color("light pink")
    else:
        t.color("light pink")
    
    t.forward(length)
    
    angle = random.randint(15, 30)
    reduction = random.uniform(0.6 , 0.8)
    
    t.left(angle)
    draw_branch(length * reduction)
    
    t.right(angle * 2)
    draw_branch(length * reduction)
    
    t.left(angle)
    t.backward(length)
# Draw the tree
draw_branch(150)

# Keep window open
turtle.done()
