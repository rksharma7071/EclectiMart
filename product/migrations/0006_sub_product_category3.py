# Generated by Django 4.2.4 on 2023-08-07 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_product_category_sub_product_category2_sub_product_category1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Product_category3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('sub_product_category2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sub_product_category2')),
            ],
        ),
    ]
