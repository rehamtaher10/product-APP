from django.db import models
from django.shortcuts import reverse
from category.models import Category
from django.contrib.auth.models import User



# Create your models here.

class Product(models.Model):
    
    "name,image,price,Decritopn,stock,created_at,updated_at"
    name=models.CharField(max_length=100,unique=True)
    image=models.ImageField(upload_to='amazon/images/', blank=True, null=True)
    description=  models.CharField(max_length=200,null=True, blank=True)
    price= models.IntegerField(default=10)
    stock=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='product_set')
    owner = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='owner')
    

    def __str__(self) :
        return f"{self.name}"
    
    def get_image_url(self):
        return f"/media/{self.image}"


    @classmethod
    def get_all_products(cls):
       return  cls.objects.all()

  
    def get_detail_url(self):
       return  reverse('product.details', args=[self.id])


    def get_delete_url(self):
       return  reverse('product.delete', args=[self.id])
    

   