# Generated by Django 4.0.2 on 2022-02-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0003_alter_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='has_drowned',
            field=models.BooleanField(default=False),
        ),
    ]
