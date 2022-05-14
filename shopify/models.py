from pydoc import describe
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from pyparsing import CaselessLiteral


class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    description = models.CharField(max_length=600)
    status = models.BooleanField()


    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    status = models.BooleanField()

    def __str__(self):
        return self.name

#class Inventory(models.Model):
    #product_id = models.ForeignKey(Product, on_delete=CASCADE)
    #Warehouse_id = models.ForeignKey(Warehouse, on_delete=CASCADE)
    #quantity = models.IntegerField(min_length=0)

    # def __str__(self):
    #     return self.name
