from django.db import models
from category.models import Category
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    
    
    def __str__(self):
        return self.name