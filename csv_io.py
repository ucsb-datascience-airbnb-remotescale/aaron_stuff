import csv

class Table(object):
    def __init__(self, filename, ignorefirst):
        self.filename = filename
        self.ignorefirst = ignorefirst
    def load_everything(self):
        output = []
        with open(self.filename,"r",encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                output.append(row)
        return output
    def load_column(self, column):
        output = []
        with open(self.filename,"r",encoding="utf-8") as file:
            reader = csv.reader(file)
            linenum = -1
            for row in reader:
                linenum += 1
                if linenum == 0:
                    if self.ignorefirst:
                        continue
                output.append(row[column])
        return output
    def load_row(self, rownum):
        # slow, avoid using this
        # starts counting from 0
        with open(self.filename,"r",encoding="utf-8") as file:
            reader = csv.reader(file)
            linenum = -1
            for row in reader:
                linenum += 1
                if linenum == rownum:
                    return row
        return None

def save_csv(filename, data):
    with open(filename,"w",encoding="utf-8") as file:
        file.truncate(0)
        writer = csv.writer(file)
        writer.writerows(data)
