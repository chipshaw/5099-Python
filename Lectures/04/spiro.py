import turtle
#import math
#import random

def drawCircles(t,size,num,decr):
    for i in range(num):
        t.circle(size)
        size=size-decr
def drawSpecial(t,size,repeat,num,decr):
  for i in range (repeat):
    drawCircles(t,size,num,decr)
    t.right(360/repeat)



def dodrawing():
    Albert = turtle.Turtle()
    Albert.speed(0)
    Albert.color('white')
    drawSpecial(Albert,100,10,10,4)

    Steve = turtle.Turtle()
    Steve.speed(0)
    Steve.color('yellow')
    drawSpecial(Steve,100,10,4,10)

    Barry = turtle.Turtle()
    Barry.speed(0)
    Barry.color('blue')
    drawSpecial(Barry,100,10,4,5)

    Terry = turtle.Turtle()
    Terry.speed(0)
    Terry.color('orange')
    drawSpecial(Terry,100,10,4,19)

    Will = turtle.Turtle()
    Will.speed(0)
    Will.color('pink')
    drawSpecial(Will,100,10,4,20)
    
def main():    
    wn = turtle.Screen()
    wn.bgcolor('black')
    #a = wn.textinput("NIM", "Name of first player:")
    dodrawing()
    wn.mainloop()
    turtle.bye()
         

main()