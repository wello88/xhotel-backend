# Generated by Django 5.0 on 2023-12-21 20:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('average_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100)),
                ('room_price', models.PositiveIntegerField()),
                ('room_type', models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room'), ('twin', 'Twin Room'), ('queen', 'Queen Room'), ('king', 'King Room'), ('suite', 'Suite'), ('connecting', 'Connecting Room'), ('adjoining', 'Adjoining Room'), ('deluxe', 'Deluxe Room'), ('executive', 'Executive Room'), ('penthouse', 'Penthouse Suite'), ('studio', 'Studio Apartment'), ('apartment', 'One-Bedroom Apartment'), ('villa', 'Villa'), ('cottage', 'Cottage'), ('chalet', 'Chalet'), ('bungalow', 'Bungalow')], max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('adults', models.PositiveIntegerField()),
                ('kids', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.room')),
            ],
        ),
    ]
