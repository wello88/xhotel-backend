# Generated by Django 4.2.8 on 2023-12-27 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('days', models.IntegerField(default=0)),
                ('nights', models.IntegerField(default=0)),
                ('massage', models.IntegerField(default=0)),
                ('safari', models.IntegerField(default=0)),
                ('camping', models.IntegerField(default=0)),
                ('seatrip', models.IntegerField(default=0)),
                ('diving', models.IntegerField(default=0)),
                ('snorkeling', models.IntegerField(default=0)),
            ],
        ),
    ]
