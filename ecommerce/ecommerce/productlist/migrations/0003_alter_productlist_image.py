# Generated by Django 4.1.5 on 2023-01-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0002_productlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to=''),
        ),
    ]
