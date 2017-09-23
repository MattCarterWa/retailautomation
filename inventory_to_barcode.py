from code import Code
import os
from papers import BarcodePage
folder = r"C:\Users\fmpho\Desktop\Fixtures"
page = BarcodePage()

for file in os.listdir(folder):
    if ".txt" in file:
        file = folder + "\\" + file
        with open(file, "r") as f:
            for line in f:
                if len(line) > 5:
                    upc = Code(line.strip())
                    # print(upc.original)
                    upc.text = upc.original
                    bc = upc.barcode()
                    print(bc.barcode_width)