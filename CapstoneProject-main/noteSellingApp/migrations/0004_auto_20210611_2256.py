# Generated by Django 3.2.4 on 2021-06-11 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noteSellingApp', '0003_auto_20210611_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_name', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('note_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='noteSellingApp.lesson')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
