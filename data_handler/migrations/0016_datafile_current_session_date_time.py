# Generated by Django 3.0.8 on 2020-07-31 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0015_memberdownloadcounter_date_inserted'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='current_session_date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]