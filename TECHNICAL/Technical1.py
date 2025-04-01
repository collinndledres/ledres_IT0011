import turtle

#Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

#Function to draw a triangle (roof)
def draw_triangle(x, y, length, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

#Function to draw a circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust position
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#Draw the house
draw_rectangle(-50, -100, 100, 100, "yellow")  # House body
draw_triangle(-75, 0, 150, "black")  # Roof
draw_rectangle(-20, -100, 40, 60, "pink")  # Door
draw_circle(-15, -75, 2, "black")  # Door knob

#Draw the tree
draw_rectangle(-150, -100, 20, 50, "brown")  # Tree trunk
draw_circle(-160, -50, 30, "green")  # Tree foliage
draw_circle(-130, -50, 30, "green")
draw_circle(-145, -25, 30, "green")
draw_circle(-145, 10, 20, "green")

#Draw the sun
draw_circle(-100, 80, 20, "red")

#Hide the turtle
turtle.hideturtle()

#Keep the window open
turtle.done()