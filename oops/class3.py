# class attributes and methods
'''
class Employee:
   name = "Bhavesh Aggarwal"
   age = "30"
# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)


'''

class Employee:
   # class attribute    
   empCount = 0  # common
   def __init__(self, name, age,count123):
      self.name = name
      self.age = age
      self.count123 = count123+1
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.name, ", Age: ", self.age ,"Count",self.count123) 
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24,0)
print()
e2 = Employee("Rajesh", 26,0)
print()
e3= Employee("Anirv",16,0)