from django.db import models

# Create your models here.
class Offers(models.Model):
    offer_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    image = models.ImageField(upload_to="myapp/images",default="")


    def __str__(self):
        return self.offer_name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    cat_img = models.ImageField(upload_to='myapp/images', default="")
    price1 = models.IntegerField(default=0)
    price2= models.IntegerField(default=0)
    desc = models.CharField(max_length=400)
    image = models.ImageField(upload_to='myapp/images', default="")


    def __str__(self):
        return self.product_name