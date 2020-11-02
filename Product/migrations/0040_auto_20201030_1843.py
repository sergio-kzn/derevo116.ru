# Generated by Django 3.1 on 2020-10-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0039_auto_20201030_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimagegroup',
            options={'ordering': ['img_group_sort'], 'verbose_name': 'Изображение (группа)', 'verbose_name_plural': 'Изображения (группы)'},
        ),
        migrations.AddField(
            model_name='productimagegroup',
            name='img_group_sort',
            field=models.IntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]