# Generated by Django 4.0 on 2022-01-01 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]
