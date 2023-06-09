# Generated by Django 4.1.7 on 2023-04-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0007_hotel_images1_hotel_images2_hotel_images3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('checkindate', models.DateField()),
                ('checkoutdate', models.DateField()),
                ('persons', models.IntegerField()),
                ('note', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
