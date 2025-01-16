lines = ["First line\n", "Second line\n", "Third line\n","python training\n","datascience\n"]
with open("example.txt", "w") as file:
    file.write("This is an example.")
    for i in lines:
        file.write(i)
#file.close()
print ("File closed successfully!!")


"""   with close 

file = open("example.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")

without close

with open("example.txt", "w") as file:
   file.write("This is an example using the with statement.")
   print ("File closed successfully!!")

"""