try:   # try with multiple catch blocks
    variable = 10 
    print( variable + "hello") 
    print(variable / 2) 
except ZeroDivisionError: 
    print("Divided by zero") 
except (ValueError, TypeError): 
    print("Type Error occured") 
