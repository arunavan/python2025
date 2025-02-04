try:  # handle all executable statements
    a=int(input('enter a'))
    b=int(input('enter b'))
    c=a/b
    print(c)
except: # to catch the exception thrown by try and display reason for excetion
    print('exception occured')  #if no exception block is ignores
    print('divide by zero')
finally:
    print('done') # either case if exception is raised or not raised 
    # resource used by try block need to be closed, file, db, socket 