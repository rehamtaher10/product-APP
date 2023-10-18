from django.db import models

# Create your models here.

class Category(models.Model):
    
    "name,image,Decritopn,created_at,updated_at"
    name=models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='category/images/', blank=True, null=True)
    description=models.CharField(max_length=300,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self) :
        return f"{self.name}"
    
    def get_image_url(self):
        return f"/media/{self.image}"
    
    @classmethod
    def get_all_categories(cls):
        return  cls.objects.all()