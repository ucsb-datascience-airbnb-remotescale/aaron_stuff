import numpy
import category_map

def stats(arr):
    output = dict()
    output["m"] = numpy.mean(arr)
    output["sd"] = numpy.std(arr)
    d = len(arr) ** 0.5
    output["se"] = output["sd"] / d
    return output

def significant(whole,sample):
    mean = sample["m"] - whole["m"]
    se = ( (sample["se"]**2) + (whole["se"]**2) ) ** 0.5
    z = mean / se
    return z

def numerocategorical(x, y):
    big = stats(y)
    xmap = category_map.category_map(x)
    org = []
    for i in range(len(xmap)):
        org.append([])
    for i in range(len(x)):
        org[xmap[x[i]]].append(y[i])
    for i in range(len(org)):
        org[i] = stats(org[i])
    for i in range(len(org)):
        org[i] = abs(significant(org[i]))
    return max(org)
