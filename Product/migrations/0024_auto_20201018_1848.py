# Generated by Django 3.1 on 2020-10-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0023_auto_20201018_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(help_text='Основное изображение товара, рекомендуемый размер 1000х700 px', upload_to='products', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_images',
            field=models.ManyToManyField(blank=True, to='Product.ProductImageGroup', verbose_name='Дополнительные изображения товара'),
        ),
        migrations.AlterField(
            model_name='productimagegroup',
            name='img_group',
            field=models.CharField(help_text='Название группы изображений, например название Товара', max_length=100, verbose_name='Дополнительные изображения'),
        ),
    ]
