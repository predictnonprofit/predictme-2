# Generated by Django 3.0.9 on 2020-08-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0028_auto_20200804_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='datahandlersession',
            name='file_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]