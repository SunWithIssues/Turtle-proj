import turtle
import random


screen = turtle.Screen() #initiates screen
turtle1 = turtle.Turtle() #initiates turtle1
turtle2 = turtle.Turtle()
turtle1.shape('turtle')

screen.bgcolor("lightblue") #bacground color
screen.title("Turtle 1 & 2") #screen windows title

cols = input('Type a color for the turtle ') #user input for turtle 1's color and size
ps = input('Input size of the turtle. Will it be 5 or 43 or somethingelse? ')
turtle1.color(cols)
turtle1.pensize(int(ps))

turtle2.color('pink')

turtle1.speed(0)
turtle1.left(3645)

turtle1.penup()
turtle1.forward(100)
turtle1.pendown()

for i in range(4): #square shaped
    turtle1.stamp()
    turtle1.forward(100)
    turtle1.left(90)

turtle1.right(180)
turtle1.forward(80)

for i in [12,5,23]: #triangle shaped
    turtle2.speed(random.randint(2,8))
    turtle2.pensize(i)
    turtle2.forward(70)
    turtle2.left(120)





screen.mainloop()
