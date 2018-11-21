# creates a mapping from a set of categories to a set of integers
# speeds up computation later

def category_map(arr):
    categories = set(arr)
    i = 0
    output = dict()
    for c in categories:
        output[c] = i
        i += 1
    return output
