# Generated by Django 4.1.7 on 2023-03-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzeria', '0003_alter_toppings_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='text',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='toppings',
            name='text',
            field=models.TextField(),
        ),
    ]
