# Generated by Django 2.2.4 on 2020-09-10 15:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cournot', '0003_remove_player_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cost',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
