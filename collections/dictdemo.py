
map=dict()
map['a']='java'
map['b']='python'
map['c']='sql'
#single item
print(map['c'])

#all items
x=map.items()
print(x)

#all items
for k,v in map.items():
    print (k,v)


d={'c':20,'b':15,'a':30}
print(d.items())
s=sorted(d.items())
print(s)

print(d.items())
for k,v in sorted(d.items()):
    print(k,v)
    print(k,v,v+100)

l=list()

for k,v in d.items():
    l.append((v,k))
print(l)
#print(l.sort(reversed=True))
print(sorted(l))

scores={'s1':90,'s2':88,'s3':67}
for k,v in scores.items():
    print(k,v)

print( sorted(  [ (k,v) for k,v in scores.items()]))
print( sorted(  [ (v,k) for k,v in scores.items()]))