from django.db import models

# Create your models here.
class fooddata(models.Model):
    name=models.CharField(max_length=255)
    photo=models.ImageField()
    price=models.IntegerField()
