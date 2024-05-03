# James Dent
# May 3, 2024
# Make initials using turtle
# P4LAB1

import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen color for first initial
t.color("orange")

# Draw first intial J
t.left(90)
t.forward(100)
t.right(180)
t.forward(200)
t.right(90)
t.forward(80)
t.right(90)
t.forward(50)

t = turtle.Turtle()

# Lift the pen up
t.penup()

# Move turtle to draw second initial
t.goto(50,50)
t.pendown()
t.pensize(10)

# Set pencolor to blue
t.pencolor("blue")

# Draw second initial
t.right(90)
t.forward(200)
t.backward(200)
t.left(90)
t.circle(-100, 180)




