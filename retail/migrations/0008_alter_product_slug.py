# Generated by Django 4.2.2 on 2023-08-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0007_product_slug_delete_productupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
