# Generated by Django 5.0 on 2023-12-30 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='hotel',
        ),
    ]