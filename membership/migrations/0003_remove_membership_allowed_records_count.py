# Generated by Django 3.0.8 on 2020-08-01 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20200625_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='allowed_records_count',
        ),
    ]
