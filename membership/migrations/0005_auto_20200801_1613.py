# Generated by Django 3.0.8 on 2020-08-01 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_membership_membership_allowed_records_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='membership_allowed_records_count',
            new_name='allowed_records_count',
        ),
    ]
