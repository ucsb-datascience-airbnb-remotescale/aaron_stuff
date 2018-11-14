import numpy

def numerical(x, y):
    c = numpy.corrcoef(x,y)
    c = c[0][1]
    return c ** 2
