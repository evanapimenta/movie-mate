# Generated by Django 4.2.4 on 2024-02-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_movie_poster_alter_show_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='staticfiles/assets/no-image.jpg', upload_to='staticfiles/assets', verbose_name='Cartaz'),
        ),
    ]
