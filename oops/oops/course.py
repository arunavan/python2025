class Course:
    cname='SMR'    # classs attribute 
    @classmethod
    def show1(cname):
        print(cname)
    def __init__(self,id,name):   # instance 
        self.id=id
        self.name=name
    def disp(self):
        print(self.id,self.name)
    @staticmethod
    def show():
        print('india is my country')
c=Course(101,'python')
print(c.cname)
print(Course.cname)
print(c.id, c.name)
c1=Course(102,'oracle')
print(c1.cname)
print(c1.id, c1.name)
c1.disp()
Course.show()
Course.show1()