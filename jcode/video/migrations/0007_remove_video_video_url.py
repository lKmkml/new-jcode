# Generated by Django 4.1.5 on 2023-02-28 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_video_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
    ]
