# Generated by Django 3.1.2 on 2020-10-10 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy_web', '0006_auto_20201010_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalinfo',
            name='gatunek',
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Horror'), (2, 'Comedy'), (4, 'Sci-fi'), (3, 'Drama'), (0, 'Different')], default=0, null=True),
        ),
    ]
