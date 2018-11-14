import csv

def check():
    g = [0]
    d = dict()
    with open("joined.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == g[0]:
                if row[68] != g[68]:
                    print(g)
                    print(row)
                    print(g[57],row[57])
                    exit()
            g = row

def get_zip():
    s = set()
    with open("joined.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            s.add(row[57])
    print(s)

check()
