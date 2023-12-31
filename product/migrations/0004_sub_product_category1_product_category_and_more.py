# Generated by Django 4.2.4 on 2023-08-07 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_sub_product_category2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_product_category1',
            name='product_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='product.product_category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub_product_category2',
            name='product_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='product.sub_product_category1'),
            preserve_default=False,
        ),
    ]
