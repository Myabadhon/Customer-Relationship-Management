# Generated by Django 3.2.7 on 2021-09-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Deliverd', 'Out For Delivred'), ('Deliverd', 'Deliverd')], max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True)),
                ('product_description', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='date',
            new_name='date_created',
        ),
    ]