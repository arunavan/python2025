a = int(input('enter deposit'))
try:
    if(a < 1000):
        raise TypeError('Minimum deposit is ')
    elif(a > 1000):
        print('thank you for deposit')
except TypeError:
    print('Type Error Occured')
if(a>1000):
    print('thank you')
print(a)

#name="ram"
#raise NameError("name is not correct")
