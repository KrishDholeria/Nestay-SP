# Generated by Django 4.1.7 on 2023-04-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_reservation_hotelemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]
