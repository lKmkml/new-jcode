# Generated by Django 4.1.5 on 2023-01-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videochapter',
            name='ordered',
            field=models.IntegerField(default=0),
        ),
    ]