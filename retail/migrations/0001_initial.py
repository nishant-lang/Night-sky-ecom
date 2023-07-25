# Generated by Django 4.2.2 on 2023-06-21 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_pic', models.FileField(upload_to='produc_item')),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('catogory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.productcatogory')),
            ],
        ),
    ]