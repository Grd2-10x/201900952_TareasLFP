
import json
import csv
import xml


def readJson():
    file = open("reg2.json",'rb') 
    data = json.load(file)
    file.close()
    print(data)
    return data





dict = readJson()
for element in dict:
    print(element)



