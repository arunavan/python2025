import pickle
a = ['luke skywalker','obi-wan kenobi', 'princess leia']
f = open('testfile','wb')
pickle.dump(a, f)
f.close()
