# Generated by Django 3.2.4 on 2021-06-11 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteSellingApp', '0004_auto_20210611_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='note_name',
            new_name='lesson_name',
        ),
    ]
