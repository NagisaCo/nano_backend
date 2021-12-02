# Generated by Django 3.2.5 on 2021-12-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='地点名称')),
                ('address', models.CharField(default='', max_length=200, verbose_name='地址')),
                ('latitude', models.FloatField(default=0, verbose_name='纬度')),
                ('longitude', models.FloatField(default=0, verbose_name='经度')),
                ('description', models.TextField(blank=True, null=True, verbose_name='地点描述')),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('is_approved', models.BooleanField(default=False, verbose_name='是否通过审核')),
                ('collection_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='animes.anime', verbose_name='动画')),
            ],
            options={
                'verbose_name': '地点信息',
                'verbose_name_plural': '地点信息',
                'db_table': 'tb_places',
            },
        ),
    ]
