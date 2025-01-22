import pickle
f = open('testfile','rb')
b = pickle.load(f)
print(b)
f.close()
