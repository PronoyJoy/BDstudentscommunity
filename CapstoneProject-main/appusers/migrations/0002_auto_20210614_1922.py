# Generated by Django 3.2.4 on 2021-06-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_id', models.CharField(max_length=100, unique=True)),
                ('buyer_name', models.CharField(max_length=20)),
                ('note_name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('mobile_banking_number', models.CharField(max_length=14)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
