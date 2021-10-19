# Generated by Django 3.2.8 on 2021-10-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='status',
            field=models.CharField(choices=[('UNVERIFIED', 'Unverified'), ('VERIFIED', 'Verified'), ('APPROVED', 'Approved'), ('INVOICED', 'Invoiced'), ('NOT_INVOICED', 'Not Invoiced')], default='UNVERIFIED', max_length=32),
        ),
    ]
