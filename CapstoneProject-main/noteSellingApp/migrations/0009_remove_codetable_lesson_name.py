# Generated by Django 3.2.4 on 2021-06-14 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteSellingApp', '0008_alter_codetable_lesson_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codetable',
            name='lesson_name',
        ),
    ]
