from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100,default='food-item')
    product_desc = models.CharField(max_length=500,default='food-item-description')
    product_price = models.CharField(max_length=10,default='0')
    product_image = models.ImageField(upload_to='shop/images',default = '')
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=15,default='')
    desc = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_Json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=12)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField(max_length=10)
    
def __str__(self):
    return self.name
