#structure 
class Employee:
    name ='ram'
    age=20
   
#object  
e=Employee()
#object with . operator 
print(e.age ,e.name)

class Manager:
    def __init__(self):   # consutructor initialize 
       self.name='ram'
       self.age=20
    def show(self):   # function to display 
        print(self.name,self.age)
m=Manager()
m.show()
    
class Course:
    def __init__(self):   # memembrs , attributes , data 
        self.id=101
        self.name='python'
        self.duration=2
    def disp(self):     # member function
        print(self.id,self.name,self.duration)
    def dispFormat(self):
        print(' Course details are {0}{1}{2}'.format(self.id,self.name,self.duration))

c=Course()
c.disp()
c.dispFormat()



