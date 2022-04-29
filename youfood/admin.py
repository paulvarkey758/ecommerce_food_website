from django.contrib import admin
from . models import category,item,cart
# Register your models here.
admin.site.register(category)
admin.site.register(item)
admin.site.register(cart)