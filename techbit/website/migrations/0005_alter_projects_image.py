# Generated by Django 3.2.7 on 2021-10-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210930_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='image', upload_to='media/products'),
        ),
    ]
