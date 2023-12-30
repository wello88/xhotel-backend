# Generated by Django 5.0 on 2023-12-30 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_room_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.hotel'),
        ),
    ]
