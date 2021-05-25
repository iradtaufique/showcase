# Generated by Django 3.2.3 on 2021-05-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='productImage')),
                ('product_usage', models.CharField(max_length=255)),
                ('sample1', models.ImageField(upload_to='productImage')),
                ('sample2', models.ImageField(upload_to='productImage')),
                ('sample3', models.ImageField(upload_to='productImage')),
            ],
        ),
    ]
