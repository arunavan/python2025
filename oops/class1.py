# defining class
#constructor   __init__
# instance variable
#class variable 
#print(type('python'))
'''
class Course:
   type1='Programming language'
   def __init__(self):
      self.id=101
      self.cname='python'
      self.duration=3
   def show(self):
      print(self.id,self.cname,self.duration)
      print(Course.type1)
 # object1 
c=Course()
print(c.id , c.cname, c.duration,c.type1, Course.type1)
print('Id is {}'.format(c.id))
print('course is {}'.format(c.cname))
print('Duration is {}'.format(c.duration))
print('Type of Course is {}'.format(Course.type1))
c.show()
c1=Course()
c1.show()


#Object2
c1=Course()
print('Id is {}'.format(c1.id))
print('course is {}'.format(c1.cname))
c1.show()


class Employee:
   'Common base class for all employees'
   def __init__(self,name,age):  #default 
      self.name = name
      self.age = age
   def disp(self):
      print(self.name,self.age)
#object
e1 = Employee('Anriv',16)  #runtime
e1.disp()
e2=Employee('Anirv11',17) #runtime 
e2.disp()

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print("name : {} age {}".format(e2.name,e2.age))


# parameterized constructor  __init__
class Smartphone:
   # constructor    
   def __init__(self, device, brand,qty,price):
      self.device = device
      self.brand = brand
      self.qty=qty
      self.price=price
   
   # method of the class
   def description(self):  #instance method
     # return 'DEvice:'+self.device+'   BRand is :'+self.brand
      #return f"{self.device} of {self.brand} supports Android 14"
      return " {}  and {} {} {}".format(self.brand,self.brand,self.qty,self.price)

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung",10,9999)
iosObj=Smartphone("compactPhone","OPPO",20,20000)
simplePhone=Smartphone("android","Motorola",30,88888)
print(phoneObj.description()) 
print(iosObj.description())
print(simplePhone.description())
'''

#class with constructor (__init__), functions disp, deposit,withdraw,getbalance
class Account:
   def __init__(self,acno,name,balance):
      self.acno=acno
      self.name=name
      self.balance=balance
   def disp(self):
      print(self.acno,self.name,self.balance)
      # adding amount with existing balance
   def deposit(self,amt):
       self.balance=self.balance+amt
   def withdraw(self,amt):
      self.balance=self.balance-amt
   def getbalance(self):
      print("Available balance is {}".format(self.balance)) 

a=Account(12345,'pythondev',10000)
a.disp()
a.deposit(2000)
a.getbalance()

a.withdraw(5000)
a.getbalance()
a.disp()

a1=Account(34567,'Anirv',50000)
a1.disp()
a1.deposit(10000)
a1.getbalance()
a1.withdraw(20000)
a1.getbalance()



