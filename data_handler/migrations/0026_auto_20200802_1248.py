# Generated by Django 3.0.8 on 2020-08-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0025_auto_20200802_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datahandlersession',
            old_name='session_date_time',
            new_name='run_modal_date_time',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='all_columns_with_dtypes',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='all_records_count',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='data_file_path',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='donor_id_column',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='file_upload_procedure',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='is_donor_id_selected',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='is_process_complete',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='selected_columns',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='selected_columns_dtypes',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='unique_id_column',
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='all_columns_with_dtypes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='all_records_count',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='data_file_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='donor_id_column',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='file_upload_procedure',
            field=models.CharField(blank=True, choices=[('local_file', 'Local File'), ('google_plus', 'Google Plus'), ('one_drive', 'One Drive'), ('dropbox', 'Dropbox'), ('none', 'None')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='is_donor_id_selected',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='is_process_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='selected_columns',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='selected_columns_dtypes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datahandlersession',
            name='unique_id_column',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
