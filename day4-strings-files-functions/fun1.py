def hello(name):
    print('my first fucntion',name)
    return
def welcome():
    print('welcome to function/ sub programming')
    return

def add(a,b)->int:
    return a+b

def hello()->None:
    print('welcome')

hello()
print(add(4,5))
    
hello('Ram')
hello('Raj')
hello('Sri')
welcome()




def sum(a):
    print(a*a)
    return
sum(5)



def getEmi(amount,duration):
    return amount/duration
print(getEmi(60000,12))


# pass by value

def swap(a,b):
    t=a
    a=b
    b=t
    print(a,b)
    return
a=5
b=6
swap(a,b)
print(a,b)

# default argument

def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

