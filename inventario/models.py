from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    name =models.CharField( max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()

class Pedido (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add= True)

class Item(models.Model):
    pedido= models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.PositiveIntegerField()
    