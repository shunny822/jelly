# Generated by Django 3.2.18 on 2023-06-15 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='attendee',
        ),
    ]
