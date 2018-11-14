import scipy
import category_map

def make_chi2_table(x_size, y_size):
    h = [0] * x_size
    h = [h]
    h = h * y_size
    return h

def fill_chi2_table(x, y, xmap, ymap, tab):
    for i in range(len(x)):
        col = xmap[x[i]]
        row = ymap[y[i]]
        tab[row][col] += 1

# def row_totals(tab):
#     output = []
#     for row in tab:
#         c = 0
#         for elem in row:
#             c += elem
#         output.append(c)
#     return output
#
# def col_totals(tab):
#     output = [0] * len(tab[0])
#     for row in tab:
#         for colnum in range(len(output)):
#             output[colnum] += row[colnum]
#     return ou
#
# def grand_total(arr):
#     c = 0
#     for elem in arr:
#         c += elem
#     return c
#
# def expected_table(tab):
#     rt = row_totals(tab)
#     ct = col_totals(tab)
#     gt = grand_total(rt)
#     output = []
#     for rownum in range(len(rt)):
#         row = []
#         for colnum in range(len(ct)):
#             v = float(rt[rownum]) * float(ct[colnum])
#             v /= float(gt)
#             row.append(v)
#         output.append(row)
#     return output
#
# def chi2(tab, et):
#     output = 0.0
#     for rownum in range(len(tab)):
#         for colnum in range(len(tab[rownum])):
#             v = (tab[rownum][colnum] - et[rownum][colnum])
#             v = v ** 2
#             v /= et[rownum][colnum]
#             output += v
#     return output

def categorical(x,y):
    xmap = category_map.category_map(x)
    ymap = category_map.category_map(y)
    tab = make_chi2_table(len(xmap),len(ymap))
    fill_chi2_table(x,y,xmap,ymap,tab)
    chi2 = scipy.stats.chi2_contingency(tab)
    return chi2[1]
