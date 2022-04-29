from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=15,unique=True)
    image=models.ImageField(upload_to="img/")

    def __str__(self):
        return self.name

class item(models.Model):
    name=models.CharField(max_length=50,unique=True,blank=False)
    image=models.ImageField(upload_to="img/")
    description=models.TextField(max_length=600)
    price=models.IntegerField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name        


class cart(models.Model):
    cartuser=models.ForeignKey(User, on_delete=models.CASCADE)
    item=models.ManyToManyField(item)

    def __str__(self):
        return self.cartuser.username

