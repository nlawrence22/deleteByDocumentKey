import sys
import csv
from jamaconfig import JamaConfig

class Read_CSV():
    def __init__(self):
        self.jamaConfig = JamaConfig()
        self.filename = self.jamaConfig.filename
        self.docKey_index = self.jamaConfig.documentKey_column - 1
        self.title_index = self.jamaConfig.name_column - 1

    def read(self):
        list = {}
        file = open(self.filename, 'rU')
        try:
            f = csv.reader(file, dialect=csv.excel_tab)
            header = ""
            for row in f:
                if header == "":
                    header = row
                else:
                    # print('Row #' + str(f.line_num) + ' ' + str(row))
                    splitRow = str(row).split(",")
                    list.__setitem__(splitRow[self.docKey_index], splitRow[self.title_index])

        finally:
            file.close()
        return list

