# Generated by Django 4.0.2 on 2022-02-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_station_manufacturer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Station',
            new_name='Chargebox',
        ),
    ]