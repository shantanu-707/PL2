import json
import csv

# def writetojson(dict):
#     with open("data.json",'w') as jf:
#         json.dump(dict,jf)
#
# def readjson(file):
#     with open(file,'r') as jf:
#         data = json.load(jf)
#         return data
#
# dict = {}
# while True:
#     intro = input("Enter new data? Y/N : ")
#     if intro == "Y":
#         name = input("Enter your name : ")
#         age = int(input("Enter your age : "))
#         salary = int(input("Enter your salary : "))
#         data = [{"name": name, "age": age, "salary": salary}]
#
#     elif intro == "N":
#         break
# writetojson(dict)
#
# jsondata = readjson("data.json")

with open("data.json") as jf:
    e = json.load(jf)

data = e

with open("jsontocsv.csv", 'w') as cf:
    cw = csv.writer(cf)
    cw.writerow(data)






