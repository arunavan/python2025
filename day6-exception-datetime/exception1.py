try:  # handle all executable statements
    a=int(input('enter a'))
    b=int(input('enter b'))
    c=a/b
    print(c)
except: # to catch the exception thrown by try and display reason for excetion
    print('exception occured')  #if no exception block is ignores
    print('divide by zero')
print('done')
#d='abc'
#print(10+int(d))
