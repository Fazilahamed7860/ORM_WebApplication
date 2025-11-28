from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):    
    name = models.CharField(max_length=100,help_text="Enter the product name")
    material = models.CharField(max_length=100,help_text="Enter the material of the product")
    colour = models.CharField(max_length=50,help_text="Enter the colour of the product")
    size = models.CharField(max_length=20,help_text="Enter the size of the product")
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'colour', 'size')





