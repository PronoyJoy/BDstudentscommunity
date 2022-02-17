# Generated by Django 3.2.4 on 2021-06-14 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteSellingApp', '0007_codetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codetable',
            name='lesson_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='noteSellingApp.lesson'),
            preserve_default=False,
        ),
    ]
