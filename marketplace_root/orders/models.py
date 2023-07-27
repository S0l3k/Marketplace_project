from django.contrib.auth.models import User
from django.db import models
from products.models import Product


# Create your models here.
class SalesOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    count = models.IntegerField()