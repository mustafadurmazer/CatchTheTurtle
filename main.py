import turtle
import random

drawing_table = turtle.Screen()
drawing_table.bgcolor("#DDA0DD")
drawing_table.title("Catch to Turtle")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.shapesize(2,2,2)
myTurtle.speed(1)

myTurtle1 = turtle.Turtle()
myTurtle1.penup()
myTurtle1.hideturtle()
myTurtle1.goto(0, 250)
myTurtle1.speed(0)
def geri_sayim(sayi):
    if sayi >= 0:
        myTurtle1.clear()
        myTurtle1.write(str(sayi), align="center", font=(25))
        sayi -= 1
        turtle.ontimer(lambda: geri_sayim(sayi),1000)
    else:
        myTurtle1.clear()
        myTurtle1.write("GAME OVER!!", align="center", font=(25))
        turtle.done()

geri_sayim(100)

while 1:
    a = random.randint(-270,270)
    b = random.randint(-310,310)
    myTurtle.setpos(b,a)







turtle.done()