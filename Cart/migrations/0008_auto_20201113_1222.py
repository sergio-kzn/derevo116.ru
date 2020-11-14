# Generated by Django 3.1 on 2020-11-13 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0007_auto_20201113_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.AddField(
            model_name='item',
            name='item_order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Cart.order', verbose_name='Заказ'),
            preserve_default=False,
        ),
    ]