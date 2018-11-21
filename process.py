import csv_io
import ds_stat_tools_n as dtn
import ds_stat_tools_cr as dtcr

def remove_absent(a,b):
    ar = []
    br = []
    for i in range(len(a)):
        if len(a[i]) == 0:
            continue
        if len(b[i]) == 0:
            continue
        ar.append(a[i])
        br.append(b[i])
    return [ar,br]

def make_numbers(arr):
    output = []
    for elem in arr:
        hold = ""
        for c in elem:
            co = ord(c)
            if (co >= 48) and (co <= 57):
                # 0 to 9
                hold += c
            elif (co == 46) or (c == 101):
                # period or e
                hold += c
        output.append(float(hold))
    return output

def do_nc():
    # runs through a csv file, printing r^2 values between the
    # columns with categorical data, and the position column
    # it prints this
    t = csv_io.Table("mv.csv",True)
    print("loading position data")
    pos = t.load_column(65)
    print("running")
    for col in [3,5,7,11,13,16,17,18,20,21,22,25,27,29,30,38,39,40,41,42,49,50,51,52,53,56,57,58,62,65]:
        da = t.load_column(col-1)
        [pos0,da0] = remove_absent(pos,da)
        pos0 = make_numbers(pos0)
        r2 = dtcr.numerocategorical(da0,pos0)
        print(col,r2)

def do_num():
    # runs through a csv file, printing r^2 values between the
    # columns with categorical data, and the position column
    # it prints this
    t = csv_io.Table("mv.csv",True)
    print("loading position data")
    pos = t.load_column(65)
    print("running")
    for col in [1,2,4,6,8,9,12,14,15,19,23,24,26,28,31,33,34,35,36,37,43,44,45,46,47,48,54,55,59,60,61,63,64,10,32]:
        da = t.load_column(col-1)
        [pos0,da0] = remove_absent(pos,da)
        pos0 = make_numbers(pos0)
        da0 = make_numbers(da0)
        r2 = dtn.numerical(da0,pos0)
        print(col,r2)
