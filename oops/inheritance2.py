# parent class
class Universe: 
   _language='english'  # protected 
   def universeMethod(self):
      print ("I am in the Universe")
      print(Universe.language)

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      print(Universe.language)
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India") 
      print(Universe.language)     

# creating instance 
person = India()
person.earthMethod()
person.indianMethod()
person.universeMethod()
u=Universe()  
u.universeMethod()
e=Earth()
e.earthMethod()
e.universeMethod()  # child isinstance parent -t
print(isinstance(e,Universe))  #parent isinstance child - false

print(isinstance(u,Earth))
print(isinstance(u,India))
print(isinstance(person,Earth))

print(isinstance(person,India))
print(isinstance(person,Earth))
print(isinstance(person,Universe))

# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 

e.earthMethod()
e.universeMethod()

u.universeMethod()