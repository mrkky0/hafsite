# Generated by Django 4.2.5 on 2023-09-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'product', 'verbose_name_plural': 'Product'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_category',
        ),
        migrations.AlterField(
            model_name='category',
            name='product_category',
            field=models.CharField(choices=[('All', 'all'), ('2', '2'), ('3', '3'), ('4', '4')], default='All', max_length=30),
        ),
    ]
