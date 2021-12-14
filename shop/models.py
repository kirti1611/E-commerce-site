from django.db import models
from django.db.models.fields import AutoField, CharField, DateField

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self) -> str:
        return self.prod_name


class Contact(models.Model):
    name=models.CharField(default='',max_length=123)
    phone=models.CharField(default='',max_length=12)
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=123)
    email=models.EmailField()
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name

