# Generated by Django 4.2 on 2023-04-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_puzzle_puzzle_status_alter_scoreboard_id_clues_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clues',
            name='clue1',
            field=models.CharField(default='Here is the first clue', max_length=300),
        ),
        migrations.AddField(
            model_name='clues',
            name='clue2',
            field=models.CharField(default='Here is the second clue', max_length=300),
        ),
    ]
