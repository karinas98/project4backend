# Generated by Django 4.2 on 2023-05-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_description'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(related_name='cart', to='products.product'),
        ),
    ]
