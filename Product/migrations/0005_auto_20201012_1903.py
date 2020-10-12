# Generated by Django 3.1 on 2020-10-12 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20201012_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['category_parent__id', 'category_sort'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_main_menu',
            field=models.BooleanField(default=0, verbose_name='Показывать в главном меню?'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Product.productcategory', verbose_name='Родительская категория'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_sort',
            field=models.IntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_title',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_url',
            field=models.SlugField(unique=True, verbose_name='Ссылка url'),
        ),
    ]
