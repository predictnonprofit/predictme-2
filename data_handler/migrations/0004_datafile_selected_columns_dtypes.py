# Generated by Django 3.0.7 on 2020-07-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0003_memberdownloadcounter_is_accept_download_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='selected_columns_dtypes',
            field=models.TextField(blank=True, null=True),
        ),
    ]