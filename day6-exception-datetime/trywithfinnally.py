
try:
   file = open("abc.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("Error: The file was not found.")
else:
   print("File read operation successful.")
finally:
   if 'file' in locals():
      file.close()
   print("File operation is complete.")