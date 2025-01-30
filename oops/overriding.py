# define parent class
class Parent: 
   def disp(self):
      print ('Calling parent method')

# define child class
class Child(Parent): 
   def show(self):
      print ('Calling child method')

# instance of child
c = Child() 
# child calls overridden method
c.disp()
c.show()

#overriding


class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def disp(self):
      print(self.name,self.salary)
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)  # parent attributes
      self.inc=inc    # current attribute
   def getSalary(self):
      return self.salary+self.inc

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))
