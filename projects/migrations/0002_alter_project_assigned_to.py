# Generated by Django 3.2.8 on 2021-10-20 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, related_name='assignees', to=settings.AUTH_USER_MODEL),
        ),
    ]
