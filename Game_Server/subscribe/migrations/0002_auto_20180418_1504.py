# Generated by Django 2.0.1 on 2018-04-18 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='name',
            new_name='subLevel',
        ),
    ]
