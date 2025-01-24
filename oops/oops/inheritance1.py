# parent class
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")
      print('super')
      print('base')


# child class
class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")
      print('sub')
      print('derived')

p=Parent()
p.parentMethod()

# instance of child
c = Child()  
# calling method of child class
c.childMethod() 
# calling method of parent class
c.parentMethod() 


class Loan:   #parent
   def loanDisp(self):
      print('parent loan')

class HousingLoan(Loan):   # child
   def hosuingLoanDisp(self):
      print('housing loan')

#l=Loan()
#l.loanDisp()

hl=HousingLoan()
hl.loanDisp()
hl.hosuingLoanDisp()

