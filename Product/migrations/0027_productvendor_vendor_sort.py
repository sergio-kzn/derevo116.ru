# Generated by Django 3.1 on 2020-10-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0026_auto_20201020_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvendor',
            name='vendor_sort',
            field=models.IntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]