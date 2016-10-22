from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    return (x**2) * (numpy.sin(x))

def g(x):
    return (2*x*numpy.sin(x)) - (x**2 - 2)*numpy.cos(x) # indefinite integral of f(x)

def integrate_simpson(x0, x1, n_panels):
    panel_width = (x1 - x0) / n_panels
    sigma = 0 # total area

    for ix in range(n_panels):
        # Find the left edge of this panel
        a = x0 + ix * panel_width
        b = a + panel_width
        m = (a + b) / 2 # Calculating midpoint value as required
        # Applying values to Simpson's Rule
        area = ((b-a)/6) * (f(a) + (4*f(m)) + f(b))
        #
        sigma += area

    return sigma

# range of panel sizes to be evaluated and bounds to integrate over
PANEL_COUNTS = [4, 8, 16, 132, 64, 128, 256, 512, 1024]
x0, x1 = 0, 2

y_data = []
ref = g(x1) - g(x0)

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
