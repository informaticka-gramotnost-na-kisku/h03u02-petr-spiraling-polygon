from numpy import *
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.pensize(1.75)

turtle.hideturtle()
turtle.degrees()
turtle.color("#1c00e1")

def polygon(n, size):
  for _ in range(n):
    turtle.forward(size)
    turtle.right(360/n)

for i in range(100):
  polygon(6, i)
  turtle.right(15)

turtle.getscreen()._root.mainloop()
