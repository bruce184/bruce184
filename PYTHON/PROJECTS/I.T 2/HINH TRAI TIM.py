import turtle

# Create a screen object
wn = turtle.Screen()

# Set the background color of the screen
wn.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()

# Set the pen color of the turtle
t.pencolor("white")

def curve():
    for _ in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor("red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

# Draw a heart
heart()

# Hide the turtle
t.hideturtle()

def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    style = ("Stencil Std", 18, "italic")
    t.write(message, font=style, align="center")

# Write the text "I LOVE YOU" on the screen
write("I", (-68, 95))
write("L", (-55, 95))
write("O", (-42, 95))
write("V", (-30, 95))
write("E", (-14, 95))
write("Y", (10, 95))
write("O", (26, 95))
write("U", (42, 95))

# Keep the window open
wn.mainloop()
