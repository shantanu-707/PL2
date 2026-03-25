# To create a file using the 'w' mode
with open("exercise.txt",'w') as fh:
    fh.write("Lorem Ipsum YAYO\n")
    print("File created.")

# To read a file using 'r' mode
with open("exercise.txt",'r') as fh:
    data = fh.read()
    print(data)

# To append to a txt file using 'a' mode
with open("exercise.txt","a") as fh:
    fh.write("Lorem Lorem Ipsum Ipsum")

with open("exercise2.txt", "r+") as fh:
    fh.write("Sample text 1234")
    data = fh.read()
    print(data)