# Generated by Django 4.1.7 on 2023-04-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hotelemail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
