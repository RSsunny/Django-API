from django.db import models

# Create your models here.
class Service(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    time= models.DateField()
    location= models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default=True)

