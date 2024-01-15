import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()

# Set up the colors for the turtle and background
t.color("blue")
screen.bgcolor("white")

# Ask the user for the shape of the turtle
shape_choice = screen.textinput("Turtle Shape", "Enter shape (arrow, turtle, circle, square, or triangle): ")
t.shape(shape_choice)

# Set up random starting point for turtle
random_x = random.randint(-300, 300)
random_y = random.randint(-300, 300)
t.penup()
t.goto(random_x, random_y)
t.pendown()

# Draw a circle somewhere on the screen
circle_radius = 100
t.penup()
circle_x = random.randint(-200, 200)
circle_y = random.randint(-200, 200)
t.goto(circle_x, circle_y - circle_radius)
t.pendown()
t.circle(circle_radius)

# Allow the user 10 moves
for _ in range(10):
    move = screen.textinput("Move", "Enter move (forward, backward, left, right): ")
    if move.lower() == "forward":
        t.forward(20)
    elif move.lower() == "backward":
        t.backward(20)
    elif move.lower() == "left":
        t.left(90)
    elif move.lower() == "right":
        t.right(90)

# Determine the turtle's position
x_pos = t.xcor()
y_pos = t.ycor()

# Determine if the turtle is inside the circle
if (x_pos - circle_x) ** 2 + (y_pos - (circle_y - circle_radius)) ** 2 <= circle_radius ** 2:
    # Turtle is inside the circle, user wins
    t.penup()
    t.goto(0, 0)  # Set turtle position to center
    t.write("Congratulations! You Win!", align="center", font=("Arial", 16, "bold"))
else:
    # Turtle is outside the circle, user loses
    t.penup()
    t.goto(0, 0)  # Set turtle position to center
    t.write("Sorry, You Lost", align="center", font=("Arial", 16, "bold"))

# Add function to keep the window open
screen.exitonclick()