# Generated by Django 4.2.5 on 2023-09-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_products_default_tag_alter_category_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.IntegerField(db_index=True, verbose_name='Product ID'),
        ),
    ]
