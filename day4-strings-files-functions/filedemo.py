name = input("Enter file:")
filehandler = open(name, "r")   # This is a file handle
text =filehandler.read()  
#print(text)
count=0
for t in text:
    count=count+1
    print(t)
print('lines',count)   
print(len(text)) 
#words = text.split()
#print(words)

#print('python'+'language')
#print('python'*3)