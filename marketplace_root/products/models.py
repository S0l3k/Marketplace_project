from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to=None)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name