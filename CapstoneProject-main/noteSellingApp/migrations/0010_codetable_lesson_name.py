# Generated by Django 3.2.4 on 2021-06-14 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteSellingApp', '0009_remove_codetable_lesson_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='codetable',
            name='lesson_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cods', to='noteSellingApp.lesson'),
        ),
    ]