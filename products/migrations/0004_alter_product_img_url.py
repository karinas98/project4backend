# Generated by Django 4.2 on 2023-04-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.ImageField(upload_to='images/creators'),
        ),
    ]
