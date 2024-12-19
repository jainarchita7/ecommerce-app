from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quatity = models.IntegerField()
    category = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quatity = models.IntegerField()

    def __str__(self):
        return  f"{self.quantity} of {self.product.name} for {self.user.username}"
    
    

