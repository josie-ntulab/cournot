# Generated by Django 2.2.4 on 2020-09-15 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cournot', '0006_player_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='history',
        ),
    ]