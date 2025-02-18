
from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return self.name

class Customer(models.Model):
    sizes=[('S','Small'),
           ('M','Medium'),
           ('L','Large')]
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)
    size  = models.CharField(max_length=1,choices=sizes,default='M')
    def __str__(self):
        return f"{self.name} - {self.product.name}"