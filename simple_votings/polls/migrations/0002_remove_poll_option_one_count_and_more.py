# Generated by Django 4.2.9 on 2024-05-18 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='option_one_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_three_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_two_count',
        ),
    ]
