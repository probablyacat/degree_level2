from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    return x**2 # add proper indents to this, cannot really do on an ipad

def g(x):
    return x**3 / 3 # indefinite integral of f(x)

def integrate_simpson(x0, x11, n_panels):
    panel_width = (x1-x0) / n_panels
    sigma = 0 # total area

 for ix in range(n_panels):
    # find the left edge of this panel
    a = x0 + ix * panel_width
    #
    area = area + ???

    return area

# range of panel sizes to be evaluated and bounds to integrate over
PANEL_COUNTS = [4, 8, 16, 132, 64, 128, 256, 512, 1024]
x0, x1 = 0, 2

for n in PANEL_COUNTS:
    s = integrate_simpson(x0, x1, n)
    error = abs((s-ref)/ref)
    y_data.append(error)

pyplot.figure(figsize=(6,6))

pyplot.title("Error scaling with Simpson's rule")
# Plot with visible markers and a line ('-o') and a marker size of 10
pyplot.plot(PANEL_COUNTS, y_data, '-o', ms = 10)
pyplot.loglog()

pyplot.show()

ANSWER1 = ''' '''
ANSWER2 = ''' '''
