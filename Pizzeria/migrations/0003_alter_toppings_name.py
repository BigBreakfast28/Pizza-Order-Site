# Generated by Django 4.1.7 on 2023-03-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzeria', '0002_pizza_name_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
