# Generated by Django 3.2.1 on 2023-12-24 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='programs',
            unique_together={('id',)},
        ),
    ]
