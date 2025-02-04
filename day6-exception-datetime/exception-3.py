a=int(input('enter deposit'))
try:  # raise is used to throw or raise exception
    if(a<1000):
        raise TypeError('Minimum deposit amount is')
except:
    print('Minimum deposit amount is')
if(a>1000):
    print('thank you for deposit')
    print(a)
