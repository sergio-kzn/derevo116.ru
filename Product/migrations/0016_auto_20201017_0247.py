# Generated by Django 3.1 on 2020-10-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_auto_20201017_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price_choice',
            field=models.BooleanField(choices=[('Простая цена', True), ('Расширенная цена', False)], default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='products/<django.db.models.query_utils.DeferredAttribute object at 0x7fe45fa65b80>/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_option',
            field=models.CharField(blank=True, default='Объем', max_length=50, null=True, verbose_name='Ценник 1 столбик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_option_price',
            field=models.CharField(blank=True, default='Цена', max_length=50, null=True, verbose_name='Ценник 2 столбик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_option_extra_1',
            field=models.CharField(blank=True, default='Расход', max_length=50, null=True, verbose_name='Ценник 3 столбик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_option_extra_2',
            field=models.CharField(blank=True, default='Цена за м2', max_length=50, null=True, verbose_name='Ценник 4 столбик'),
        ),
    ]
