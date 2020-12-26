import pickle

class ABC:
    arr = [1,2,3,4]
    pass

# arr = pickle.load(open("arr.bin", "rb"))
abc = pickle.load(open("abc.pickle", "rb"))

# print(arr)
# print(type(arr))

print(abc.arr)