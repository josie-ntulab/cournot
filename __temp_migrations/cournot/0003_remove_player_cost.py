# Generated by Django 2.2.4 on 2020-09-10 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cournot', '0002_player_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cost',
        ),
    ]
