name = input("Enter file:")
a = open(name, "r")   # This is a file handle
text = a.read()  
print(text)
words = text.split()
print(words)

print('python'+'language')
print('python'*3)