
# static method , class method
# instance method
class Product:  #classs attributes
    id=10
    address='hyd'
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
        #instance method
    def ishow(self):
        print(self.name,self.qty,self.price)
        print(Product.id,Product.address)
    @classmethod  
    def show(cls):
        cls.mname='sony'
        print(cls.mname)
        print(cls.address)
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


