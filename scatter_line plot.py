"""
scatter plot and line plot samples
"""

#character color
#b blue
#g green
#r red
#c cyan
#m magenta
#y yellow
#k black
#w white

#line style
#plot(x,y, '--')
#Other linestyles you can use can be found on the Matplotlib webpage http://
#matplotlib.sourceforge.net/api/pyplot api.html#matplotlib.pyplot.plot.

#marker types:
#'s' square marker
#'p' pentagon marker
#'*' star marker
#'h' hexagon1 marker
#'H' hexagon2 marker
#'+' plus marker
#'x' x marker
#'D' diamond marker
#'d' thin diamond marker
#'o' circle marker

#****************************************************
# scatterplot.py
import numpy as np
import pylab as pl
# Make an array of x values
x = [1, 2, 3, 4, 5]
# Make an array of y values for each x value
y = [1, 4, 9, 16, 25]
# use pylab to plot x and y as "r" red "D" diamonds "--" dashed line
pl.plot(x, y, 'rD--')
#plot limits
pl.xlim(-2, 10)
pl.ylim(0, 27)

# show the plot on the screen
pl.xlabel('x-axis')
pl.ylabel('y-axis')
pl.title('Title Plot')
pl.show()

#****************************************************

# lineplotFigLegend.py
import numpy as np
import pylab as pl
# Make x, y arrays for each graph
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]
# use pylab to plot x and y : Give your plots names
plot1 = pl.plot(x1, y1, 'r')
plot2 = pl.plot(x2, y2, 'go')
# give plot a title
pl.title('Plot of y vs. x')
# make axis labels
pl.xlabel('x axis')
pl.ylabel('y axis')
# set axis limits
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.)
# make legend
pl.legend([plot1, plot2], ('red line', 'green circles'), 'best', numpoints=1)
# show the plot on the screen
pl.show()
