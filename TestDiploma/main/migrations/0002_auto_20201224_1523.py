# Generated by Django 3.1.4 on 2020-12-24 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['price']},
        ),
        migrations.AlterModelTable(
            name='property',
            table='location',
        ),
    ]