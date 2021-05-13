from django.db import models

# Create your models here.
class fooddata(models.Model):
    name=models.CharField(max_length=255,blank=False)
    photo=models.ImageField(upload_to="img/")
    discription=models.TextField(blank=False,null=True)
    price=models.IntegerField(blank=False)
    category=models.CharField(max_length=200,blank=False,choices=[('sweets','sweets'),('fastfood','fastfood'),('meals','meals'),('snacks','snacks'),('curry','curry')])

    def __str__(self):
        return self.name
