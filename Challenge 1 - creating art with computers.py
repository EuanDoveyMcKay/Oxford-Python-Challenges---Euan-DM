import numpy as np
import matplotlib.pyplot as plt

FontDictGraphs = {"family":"calibri", "size":10}
FontDictTitle = {"family":"calibri", "size":40}

#-Plotting Circle-----------------------------------------------------------------------------------------------------------------------------#

t = np.linspace(0,2*np.pi)
# Linearly spaces points of range between 0 and 2pi #
x = np.cos(t)
y = np.sin(t)

plt.subplot(1,3,1)
plt.plot(x,y, "o:r", ms=3, mfc="b", mec="b")
# "o" is the point marker, ":" is the join line type, "r" is the colour, ms is "marker size" #
# "mec" is "marker edge colour". etc. #
plt.title("Circle", fontdict=FontDictGraphs)

#-Plotting Fermat's Spiral---------------------------------------------------------------------------------------------------------------------#

t = np.linspace(0,8*np.pi,500)
# args are: start, stop, NumPointsUsed (default 50) #

xPositive = (t**0.5) * np.sin(t)
yPositive = (t**0.5) * np.cos(t)
xNegative = -(t**0.5) * np.sin(t)
yNegative = -(t**0.5) * np.cos(t)
# Using formula: x = +- t^0.5 sin(t), and y = +- t^0.5 cos(t) #

plt.subplot(1,3,2)
# args: rows,cols,pltNum #
plt.plot(xPositive,yPositive,xNegative,yNegative)
plt.title("Fermat's Spiral", fontdict=FontDictGraphs)

#-Plotting Butterfly curve----------------------------------------------------------------------------------------------------------------------#
t = np.linspace(0,12*np.pi,500)
# According to WikiPedia, t needs to be between 0 and 12pi #

xBFly = np.sin(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )
yBFly = np.cos(t) * ( (np.exp(np.cos(t)) ) - ( 2*np.cos(4*t) ) - ( (np.sin(t/12))**5 ) )
# Using parametric equations from WikiPedia: https://en.wikipedia.org/wiki/Butterfly_curve_(transcendental) #

plt.subplot(1,3,3)
plt.plot(xBFly,yBFly)
plt.title("Butterfly curve", fontdict=FontDictGraphs)

#-Showing Graphs--------------------------------------------------------------------------------------------------------------------------------#

plt.suptitle("Oxford maths challenge 1", fontdict=FontDictTitle)
plt.show()