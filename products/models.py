from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    minimum_age_appropriate = models.IntegerField(default=0, blank=False)
    maximum_age_appropriate = models.IntegerField(default=-1, blank=False)
    
  
    def age_range(self): 
      if self.maximum_age_appropriate==-1:
        return "Ages " +str(self.minimum_age_appropriate) +" up"
      elif self.minimum_age_appropriate!=-1:
        return "Ages " +str(self.minimum_age_appropriate)+" to "+str(self.maximum_age_appropriate) 
      elif self.minimum_age_appropriate==self.maximum_age_appropriate:
        return "Age " + str(self.maximum_age_appropriate)

    def __str__(self):
        return f"Product {self.name}, price {self.price:.02f}"
