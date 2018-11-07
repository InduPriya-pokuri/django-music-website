# Generated by Django 2.0.2 on 2018-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180710_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
        migrations.AddField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]