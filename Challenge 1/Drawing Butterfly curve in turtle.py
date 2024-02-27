import turtle
import numpy as np

Colours = ["#e81416","#ffa500","#faeb36","#79c314","#487de7","#4b369d","#70369d"]
# These are just the colours of rainbow: red, orange, yellow, green, blue, indigo, violet

wn = turtle.Screen()
wn.screensize(1920,1080)

t = np.linspace(0,12*np.pi,1000)
# According to WikiPedia, t needs to be between 0 and 12pi
# The last arg (1000) is the number of points it plots to (essentially the slots it lin spaces out to)

xBFly = 197*(np.sin(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )) - 125
yBFly = 197*(np.cos(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )) - 125
# Using parametric equations from WikiPedia: https://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)
# I had to multiply by 197 to make it larger as to fit the whole of a 1920x1080 monitor, and I also took it down by 125 pixels to fit onto the screen (wings went off otherwise)

Pen = turtle.Turtle()
Pen.hideturtle()

Pen.speed(0)
ColourIndex = 0
# The colour index value allows me to linearly cycle through the list of colours in my array by adding one

Pen.color(Colours[ColourIndex])
Pen.penup()
Pen.goto(xBFly[0],xBFly[0])
Pen.pendown()
Pen.width(2)

for i in range(len(xBFly)):
    Pen.goto(xBFly[i],yBFly[i])
    ColourIndex = (ColourIndex +1) % 7
    # The MOD 7 is so that the index never exceeds the possible list indexes (1-6)... it basically is just to stop index errors
    Pen.color(Colours[ColourIndex])

wn.mainloop()