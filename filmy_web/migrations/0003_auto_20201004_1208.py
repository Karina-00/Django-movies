# Generated by Django 3.1.2 on 2020-10-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy_web', '0002_auto_20201004_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
    ]