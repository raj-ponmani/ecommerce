# Generated by Django 4.1.3 on 2022-11-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
