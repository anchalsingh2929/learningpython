class rectangle():


    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b
    
    def parametre(self):
        return 2*(self.l+self.b) 
    
a=rectangle(12,32)

print(a.l)
print(a.b)
print(a.area())
print(a.parametre())
