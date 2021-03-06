# Generated by Django 3.1.2 on 2020-10-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy_web', '0005_auto_20201010_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Comedy'), (1, 'Horror'), (0, 'Different'), (3, 'Drama'), (4, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('films', models.ManyToManyField(to='filmy_web.Film')),
            ],
        ),
    ]
