courses=('java','python','sql')
print(courses[1])
#courses[2]='plsql'    tuple is immutable 
print(courses[2])
for i in courses:
    print(i)

l=list()
print(dir(l))  # can be modified  -mutable
t=tuple()
print(dir(t))  # cannot be modified - immutable

(x,y)=(100,200)
print(x)
print(y)
z=(100,200,"java","python","python",200)
print(z)


print((1,2,3) < (5,6,7))
print((0,1,200000) < (0,3,4))