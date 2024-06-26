# Generated by Django 4.2.5 on 2023-09-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_products_delete_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=30)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Category',
            },
        ),
    ]
