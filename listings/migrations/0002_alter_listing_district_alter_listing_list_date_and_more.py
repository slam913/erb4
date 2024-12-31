# Generated by Django 4.2.17 on 2024-12-31 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='district',
            field=models.CharField(choices=[('_', 'All Districts'), ('Islands', 'Islands'), ('Kwai_Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai_Kung', 'Sai Kung'), ('Sha_Tin', 'Sha Tin'), ('Tai_Po', 'Tai Po'), ('Tsuen_Wan', 'Tsuen Wan'), ('Tuen_Mun', 'Tuen Mun'), ('Yuen_Long', 'Yuen Long'), ('Kowloon_City', 'Kowloon City'), ('Kwun_Tong', 'Kwun Tong'), ('Sham_Shui_Po', 'Sham Shui Po'), ('Wong_Tai_Sin', 'Wong Tai Sin'), ('Yau_Tsim_Mong', 'Yau Tsim Mong'), ('Central_&_Western', 'Central & Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan_Chai', 'Wan Chai')], max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
