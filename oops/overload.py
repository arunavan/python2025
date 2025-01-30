
#method/ function overloading - polymorphism
class Polygon:
    #area
    
        

    def area1(self,s:int):
        return s*s
    #area
    def area2(self,r:float):
        return 3.142*r*r
    def area3(self,l:float,b:int):
        return l*b
   
p=Polygon()
print('area of square',p.area1(5))
print('area of cicrcle',p.area2(4.5))
print('area of rectangle',p.area3(5.3,6))
    