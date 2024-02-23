import turtle
import numpy as np

wn = turtle.Screen()
wn.screensize(1920,1080)

t = np.linspace(0,12*np.pi,2000)
# According to WikiPedia, t needs to be between 0 and 12pi #

xBFly = np.sin(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )
yBFly = np.cos(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )
# Using parametric equations from WikiPedia: https://en.wikipedia.org/wiki/Butterfly_curve_(transcendental) #

Pen = turtle.turtle()
Pen.penup()
Pen.goto(xBFly[0],xBFly[0])

for i in range(len(xBFly)):
    Pen.goto(xBFly[i],yBFly[i])

wn.mainloop()

# THIS CODE IS UNTESTED!!!
# I am away from home rn working on an amazon ec2 instance, but none of my command line commands work (including pip), so I cannot install any of my needed libraries.
# Hence the lack of testing.