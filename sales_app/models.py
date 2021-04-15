from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRODUCT_CHOISE = (
   ('TV','tv'),
   ('IPAD','ipad'),
   ('PLAYSTATION','playstation')
)

class SaleDataFromCsv(models.Model):
   product = models.CharField(max_length=11,choices=PRODUCT_CHOISE)

   quantity = models.PositiveIntegerField()
   total = models.FloatField(blank=True)
   updated_time = models.DateTimeField(auto_now=True)
   created_data = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.product} || quantity {self.quantity}'

   #this fucntion calculate the price of product with the quantity
   def save(self,*args,**kwargs):
      price =None #initital price null

      if self.product =='TV':
         price = 559.99

      elif self.product =='IPAD':
         price = 400.99
      elif self.product =='PLAYSTATION':
         price = 464.99
      else:
         pass
      self.total = price*self.quantity
      super().save(*args,**kwargs)






