# Generated by Django 5.1.3 on 2024-11-28 05:32

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('cust_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_catogery',
            new_name='product_category',
        ),
    ]
