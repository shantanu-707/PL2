import pickle

lst = [1,2,3,4,5,6,7]
img = "image.png"
with open ("binary.dat", 'wb') as fh:
    pickle.dump(lst,fh)
    pickle.dump(img,fh)

with open("binary.dat",'rb') as fh:
    data = pickle.load(fh)
    print(data)


