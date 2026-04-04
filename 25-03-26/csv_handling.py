import csv

data = [['Name', 'Age'], ['Alice', '25'], ['Bobby', '30']]
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('output.csv','r') as fh:
    count = 0
    rr = csv.reader(fh)
    for i in rr:
        count +=1
    print(count-1)

