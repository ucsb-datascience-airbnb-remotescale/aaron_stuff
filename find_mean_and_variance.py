import numpy as np
import csv

def find_mv(positions):
    m = np.mean(positions)
    if len(positions) < 3:
        return [m,0]
    v = np.std(positions,ddof=1) ** 2
    return [m,v]

def bad_sort(data,col):
    hold = data[:]
    p = []
    output = []
    while len(hold) != 0:
        p = []
        match = 10.0**10.0
        for i in range(len(hold)):
            if hold[i][col] < match:
                match = hold[i][col]
        for i in range(len(hold)):
            if hold[i][col] == match:
                output.append(hold[i])
            else:
                p.append(hold[i])
        hold = p
    return output

def remove_zeros(data):
    output = []
    for row in data:
        if row[-1] != 0:
            output.append(row)
    return output

def keep_low_variance(data):
    vars = []
    for row in data:
        vars.append(row[-1])
    cutoff = np.mean(vars) - np.std(vars)
    output = []
    for row in data:
        if row[-1] <= cutoff:
            output.append(row)
    return output

def save_csv(filename, data):
    with open(filename,"w",encoding="utf-8") as file:
        file.truncate(0)
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    # this function will read a raw data file in csv format
    # it will write a data file that contains similar data, replacing the last
    # 4 columns with 2 columns (mean and sstd of position) for each listing
    # it sorts by mean position, best at the top, worst at the bottom
    id = "-1"
    hold = []
    positions = []
    output = []
    first = True
    with open("joined.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if first:
                first = False
                continue
            if row[0] == id:
                positions.append(float(row[66]))
            else:
                if id == "-1":
                    pass
                else:
                    output.append(hold+find_mv(positions))
                id = row[0]
                hold = row[:65]
                positions = []
                positions.append(float(row[66]))
    output.append(hold+find_mv(positions))
    print("sorting")
    output = bad_sort(output,-1)
    print("remove zeros")
    output = remove_zeros(output)
    print("removing high variance")
    output = keep_low_variance(output)
    print("sorting by position")
    output = bad_sort(output,-2)
    save_csv("mv.csv",output)

main()
