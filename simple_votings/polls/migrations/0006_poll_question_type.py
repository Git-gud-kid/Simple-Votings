# Generated by Django 4.2.9 on 2024-05-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_poll_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='question_type',
            field=models.CharField(choices=[('single', 'Single Choice'), ('multiple', 'Multiple Choice')], default='single', max_length=10),
        ),
    ]