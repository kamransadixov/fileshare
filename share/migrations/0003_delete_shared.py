# Generated by Django 3.0.3 on 2020-03-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_shared'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shared',
        ),
    ]