import turtle

polygon=turtle.Turtle()

num_sides=6
side_lenght=90
angle=360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
    polygon.pencolor("red")

turtle.done()
