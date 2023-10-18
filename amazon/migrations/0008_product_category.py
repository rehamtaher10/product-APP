# Generated by Django 4.2.6 on 2023-10-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_category_image'),
        ('amazon', '0007_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amazon', to='category.category'),
        ),
    ]