from django.db import models

# Create your models here.
class fooddata(models.Model):
    name=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="img/")
    price=models.IntegerField()
    category=models.CharField(max_length=200,choices=[('sweet','sweet'),('fast_food','fast food'),('meals','meals'),('snacks','snacks'),('curry','curry')])
