# Generated by Django 4.2.6 on 2023-10-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Decritopn',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
