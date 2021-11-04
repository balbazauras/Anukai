# Generated by Django 3.2.7 on 2021-11-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=123, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'slug')},
        ),
    ]
