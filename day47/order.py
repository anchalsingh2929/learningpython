class item():
  
  def __init__(self,quantity):
     self.quantity=quantity
     self.name="mouse"
     self.price=2500


  def rate(self):
     return self.quantity*self.price
      
vipin=item(5)
print(dir (vipin))
print(vipin.rate())
print(vipin.name)









































def rate(qty, pri, nam):
   return qty*pri

vipin = rate(5, 100, "mouse")




















vipin


















anchal = rate(5, 2500)