# Generated by Django 4.1.7 on 2023-03-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_eu',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=10, null=True, verbose_name='Размер_eu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, choices=[('pcs', 'штук'), ('pack', 'уп'), ('kg', 'кг')], max_length=10, null=True, verbose_name='Ед. изм'),
        ),
    ]
