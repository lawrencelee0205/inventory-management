from django.db import models

# Create your models here.
class Store(models.Model):
    store_name=models.CharField(max_length=200)
    pass

class Material(models.Model):
    price=models.DecimalField()
    name=models.CharField(max_length=200)
    pass

class MaterialQuantity(models.Model):
    quantity=models.IntegerField
    ingredient=models.ForeignKey(Material,on_delete=models.CASCADE)
    pass

class User(models.Model):
    store=models.ForeignKey(Store,models.CASCADE)
    token=models.CharField(max_length=200)

class MaterialStock(models.Model):
    store=models.ForeignKey(Store)
    material=models.ForeignKey(Material,on_delete=models.CASCADE)
    current_capacity=models.IntegerField()
    max_capacity=models.IntegerField()
    pass

class Product(models.Model):
    name=models.CharField(max_length=100)
    material_quantity=models.ForeignKey(MaterialQuantity)
    pass