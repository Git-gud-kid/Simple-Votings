# Generated by Django 4.2.9 on 2024-05-19 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_poll_option_one_count_poll_option_three_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
