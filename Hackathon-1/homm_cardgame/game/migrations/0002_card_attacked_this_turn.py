# Generated by Django 4.2 on 2023-04-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='attacked_this_turn',
            field=models.BooleanField(default=False),
        ),
    ]