# Generated by Django 4.2.6 on 2023-10-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/images/'),
        ),
    ]
