# Generated by Django 3.2.5 on 2021-12-02 07:28

from django.db import migrations, models
import nano_backend.utils.storage


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_auto_20211130_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='cover',
            field=models.ImageField(storage=nano_backend.utils.storage.ImageStorage, upload_to='animes/cover', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='cover_small',
            field=models.ImageField(storage=nano_backend.utils.storage.ImageStorage, upload_to='animes/cover_small', verbose_name='封面图片(小)'),
        ),
    ]
