# Generated by Django 3.2.4 on 2021-06-15 15:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0002_auto_20210614_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
