# Generated by Django 4.2.2 on 2023-06-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.CharField(),
        ),
    ]
