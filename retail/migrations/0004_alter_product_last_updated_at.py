# Generated by Django 4.2.2 on 2023-08-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0003_product_last_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
