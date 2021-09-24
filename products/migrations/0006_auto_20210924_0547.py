# Generated by Django 3.2.7 on 2021-09-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_usage',
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]