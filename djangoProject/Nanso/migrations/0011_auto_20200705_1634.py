# Generated by Django 3.0.7 on 2020-07-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nanso', '0010_product_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='product-pics'),
        ),
    ]
