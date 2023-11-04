import turtle
import random

drawing_table = turtle.Screen()
drawing_table.bgcolor("light blue")
drawing_table.title("Catch to Turtle")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.fillcolor("light green")
myTurtle.shapesize(2,2,2)
myTurtle.speed(0)
myTurtle.penup()

myTurtle1 = turtle.Turtle()
myTurtle1.penup()
myTurtle1.hideturtle()
myTurtle1.goto(0, 250)
myTurtle1.speed(0)

myTurtle2 = turtle.Turtle()
myTurtle2.penup()
myTurtle2.hideturtle()
myTurtle2.goto(0,200)
myTurtle2.speed(0)

myTurtle3 = turtle.Turtle()
myTurtle3.penup()
myTurtle3.hideturtle()
myTurtle3.goto(0, 200)
myTurtle3.speed(0)
myTurtle3.write(f"Kaplumbağaya Tıklama Sayısı : 0" ,align = "center" , font = (25))
def geri_sayim(sayi):
    if sayi >= 1:
        myTurtle1.clear()
        myTurtle1.write(str(sayi), align = "center", font = (25))
        sayi -= 1
        turtle.ontimer(lambda: geri_sayim(sayi),1000)
    else:
        myTurtle1.clear()
        myTurtle1.write("GAME OVER!!", align="center", font = (25))
        myTurtle.hideturtle()
        turtle.done()

geri_sayim(10)
sayac = 0

def setposturtle():
    a = random.randint(-270, 270)
    b = random.randint(-310, 310)
    myTurtle.setpos(b, a)
    turtle.ontimer(setposturtle, 750)

def tiklama(x ,y):
    myTurtle2.clear()
    myTurtle3.clear()
    global sayac
    sayac += 1
    myTurtle2.write(f"Kaplumbağaya Tıklama Sayısı : {sayac}" ,align = "center" , font = (25))

setposturtle()
myTurtle.onclick(tiklama)


turtle.done()