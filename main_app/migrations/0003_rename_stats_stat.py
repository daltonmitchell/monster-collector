# Generated by Django 4.0.4 on 2022-07-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_stats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stats',
            new_name='Stat',
        ),
    ]
