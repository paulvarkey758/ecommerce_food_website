# Generated by Django 4.0.3 on 2022-04-05 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youfood', '0004_delete_videodemo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='cartuser',
        ),
    ]
