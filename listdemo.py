courses=['java','python','spring','angular','react','mogodb']
fee=[455,234324,234234]
print("=====================")
print(sum(fee))
print(courses+fee)

#print(courses[2:5])
#print(courses[:3])
print(courses[2:])
print(courses[:])
print(type(courses))
print(dir(courses))
for i in range(len(courses)):
    c=courses[i]
    print(c)
    

slist=list()
slist.append('raj')
slist.append('ram')
slist.append('kiran')
print(slist)
print('ram' in slist)
print('jim' in slist)
slist.sort()
print(slist)
print(max(slist), min(slist))

message='good morning'
print(message.split())
address='89/madhaur/hyd/india'
print(address.split('/'))