# Generated by Django 3.0.9 on 2020-08-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0029_datahandlersession_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datahandlersession',
            name='data_handler_session_label',
            field=models.CharField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
