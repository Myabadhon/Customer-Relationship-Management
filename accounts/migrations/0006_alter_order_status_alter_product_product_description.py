# Generated by Django 4.0.2 on 2022-02-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210909_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivered', 'Out For Delivred'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
