# Generated by Django 3.1 on 2020-10-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_count',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_vendor',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='_productcategory_category_parent_+', to='Product.ProductCategory'),
        ),
    ]
