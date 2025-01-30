# parent class
class Parent: 
   def __init__(self,name):
      self.name='ram'
   def parentMethod(self):
      print ("Calling parent method")
      print('super')
# child class
class Child(Parent): 
   def __init__(self,address):
      self.address='US'
   def childMethod(self):
      print ("Calling child method")
      print('sub')
p=Parent('raj')
p.parentMethod()
# instance of child
c = Child('US')  
# calling method of child class
c.childMethod() 
# calling method of parent class
c.parentMethod() 