# Generated by Django 4.2.4 on 2024-02-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='catalog/assets', verbose_name='Cartaz'),
        ),
    ]
