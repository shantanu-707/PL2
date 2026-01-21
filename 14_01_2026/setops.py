s1 = {1,2,3,4}
s2 = {3,4,5,6}

for i in s1:
    print(i)

myunion = s1|s2
print(myunion)

myintersection = s1&s2
print(myintersection)

difference = s1-s2
print(difference)
