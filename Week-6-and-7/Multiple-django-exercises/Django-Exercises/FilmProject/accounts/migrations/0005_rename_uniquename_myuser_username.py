# Generated by Django 4.2 on 2023-05-11 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_myuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='uniquename',
            new_name='username',
        ),
    ]
