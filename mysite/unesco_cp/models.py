from django.db import models
from decimal import Decimal

class Category(models.Model) :
    categoryname = models.CharField(max_length=128, unique=True, default=None, null=True)
    
    def __str__(self) :
        return self.categoryname

class States(models.Model) :
    statename = models.CharField(max_length=128, unique=True, default=None, null=True)

    def __str__(self) :
        return self.statename

class Region(models.Model) :
    regionname = models.CharField(max_length=128, unique=True, default=None, null=True)

    def __str__(self) :
        return self.regionname

class Iso(models.Model) :
    isoname = models.CharField(max_length=128, unique=True, default=None, null=True)

    def __str__(self) :
        return self.isoname

class Site(models.Model):
    name = models.CharField(max_length=128, null=True, default=None)
    description = models.CharField(max_length=128, null=True, default=None)
    justification = models.CharField(max_length=128, null=True, default="NA")
    year = models.CharField(max_length=128,null=True, default=None)
    longitude = models.CharField(max_length=128, null=True, default=None)
    latitude = models.CharField(max_length=128, null=True, default='0.0')
    area_hectares = models.CharField(max_length=128, null=True, default='0.00')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True, default=None)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default=None)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True, default=None)

    #def __str__(self) :
        #return "Category: "+str(self.category.id)
