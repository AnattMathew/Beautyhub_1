# Generated by Django 5.1 on 2024-11-07 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_sex_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Sex',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Size',
        ),
    ]
