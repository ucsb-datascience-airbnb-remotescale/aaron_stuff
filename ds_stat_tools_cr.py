import numpy
import category_map

# maps categories to the mean of each category
# finds and returns r^2
def numerocategorical(x, y):
    xmap = category_map.category_map(x)
    org = []
    for i in range(len(xmap)):
        org.append([])
    for i in range(len(x)):
        org[xmap[x[i]]].append(y[i])
    for i in range(len(org)):
        org[i] = numpy.mean(org[i])
    xa = []
    for i in range(len(x)):
        xa.append(org[xmap[x[i]]])
    c = numpy.corrcoef(xa,y)
    c = c[0][1]
    return c ** 2
