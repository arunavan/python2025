i = 7
if isinstance(i, int):
 i += 1
 print(i)
elif isinstance(i, str):
 i = int(i)
 i += 2
 print(i)