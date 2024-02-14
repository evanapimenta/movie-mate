# Generated by Django 4.2.4 on 2024-02-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_catalog_options_alter_genre_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='assets/no-image.jpg', upload_to='static/assets', verbose_name='Pôster'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveIntegerField(max_length=4, verbose_name='Release year'),
        ),
        migrations.AlterField(
            model_name='show',
            name='poster',
            field=models.ImageField(default='no-image.jpg', upload_to='static/assets', verbose_name='Pôster'),
        ),
    ]