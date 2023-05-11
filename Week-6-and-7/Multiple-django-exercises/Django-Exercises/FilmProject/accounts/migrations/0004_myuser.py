# Generated by Django 4.2 on 2023-05-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uniquename', models.CharField(max_length=30, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('film_reviewed', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
