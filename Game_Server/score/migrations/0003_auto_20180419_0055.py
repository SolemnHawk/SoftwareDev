# Generated by Django 2.0.1 on 2018-04-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_auto_20180419_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
