# Generated by Django 3.2.8 on 2021-10-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_tracker_pause_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='pause_state',
        ),
        migrations.AddField(
            model_name='tracker',
            name='timer_state',
            field=models.CharField(choices=[('paused', 'pause'), ('running', 'run')], default='paused', max_length=32),
        ),
    ]