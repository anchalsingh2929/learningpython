class circle:

    def __init__(self,r):
        self.r=r

    def area(self):
      return 3.14*self.r**2
    
    def parametre(self):
       return 2*3.14*self.r


a=circle(10)    
print(a.parametre())
b=circle(3)
print(b.area())