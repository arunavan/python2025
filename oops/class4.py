
# static method , class method
# instance method
class Product:  #classs attributes
    id=10
    address='hyd'
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
        #instance method  spesific to object
    def ishow(self):
        print(self.name,self.qty,self.price,self.id,self.address)
        print(Product.id,Product.address)
    @classmethod    #common for all objects
    def show(cls):
        cls.mname='sony'
        print(cls.mname)
        print(cls.address)
        print(cls.id)
        Product.id=Product.id+20
        print(cls.id)
    @staticmethod
    def disp():
        print(Product.mname)
        print(Product.address)
        Product.id=Product.id+20
        print(Product.id)
        
p=Product('box',90,999)
p.ishow() #instance method
print(p.name,p.price,p.qty)
p.show()
p.disp()


