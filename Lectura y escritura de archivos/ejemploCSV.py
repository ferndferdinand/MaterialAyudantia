import csv

#reader
file = open("ejemploReader.csv","r")
reader = csv.reader(file)

for row in reader:
    #print(row)
    print(row[0])
file.close()

print()
#DictReader
file = open("ejemploReader.csv","r")
reader = csv.DictReader(file,fieldnames = ["elem0","elem1","elem2"])

for row in reader:
    print(row["elem0"])
file.close()

print()
#Sin fieldnames
file = open("ejemploDictReader.csv","r")
reader = csv.DictReader(file)

for row in reader:
    print(row)
file.close()



#write
"""
file = open("ejemploWriter.csv","w",newline= '')#Cambiar a 'a' si ya existe el archivo
write = csv.writer(file)
write.writerow(["row1 column 1", "row1 column 2", "row1 column 3"])
file.close()

file = open("ejemploWriter.csv","a",newline= '')
write = csv.writer(file)
write.writerow(["row2 column 1", "row2 column 2", "row2 column 3"])
file.close()

"""
with open("ejemploWriter.csv","w",newline= '') as file:
    write = csv.writer(file)
    write.writerow(["row1 column 1", "row1 column 2", "row1 column 3"])

with open("ejemploWriter.csv","a",newline= '') as file:
    write = csv.writer(file)
    write.writerow(["row2 column 1", "row2 column 2", "row2 column 3"])



#DictWriter
file = open("ejemploDictWriter.csv","w",newline= '')#Cambiar a 'a' si ya existe el archivo
writer = csv.DictWriter(file, fieldnames =["column1", "column2", "column3"])
writer.writeheader()
writer.writerow({"column1":"row1 column 1","column2": "row1 column 2","column3": "row1 column 3"})
writer.writerow({"column1":"row2 column 1","column2": "row2 column 2","column3": "row2 column 3"})
file.close()

file = open("ejemploDictWriter.csv","a",newline= '')
writer = csv.DictWriter(file, fieldnames =["column1", "column2", "column3"])
writer.writerow({"column1":"row3 column 1","column2": "row3 column 2","column3": "row3 column 3"})
writer.writerow({"column1":"row4 column 1","column2": "row4 column 2","column3": "row4 column 3"})
file.close()















