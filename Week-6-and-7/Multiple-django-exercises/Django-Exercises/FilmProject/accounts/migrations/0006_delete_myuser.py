# Generated by Django 4.2 on 2023-05-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_uniquename_myuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
