import csv

def readCsv():
    file = open("reg3.csv",'rb') 
    data = csv.load(file)
    file.close()
    print(data)
    return data





dict = readCsv()
for element in dict:
    print(element)