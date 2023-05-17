# Generated by Django 4.2 on 2023-05-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='films_watched',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='films_reviewed',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]