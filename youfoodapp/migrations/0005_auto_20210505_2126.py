# Generated by Django 3.1.7 on 2021-05-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youfoodapp', '0004_auto_20210505_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddata',
            name='category',
            field=models.CharField(choices=[('sweet', 'sweet'), ('fast_food', 'fast food'), ('meals', 'meals'), ('snacks', 'snacks'), ('curry', 'curry')], max_length=200),
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='photo',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
