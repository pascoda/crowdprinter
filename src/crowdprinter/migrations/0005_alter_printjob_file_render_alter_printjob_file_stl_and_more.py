# Generated by Django 5.1.2 on 2024-10-30 17:51

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("crowdprinter", "0004_printer_alter_printjob_file_stl_printjobfile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printjob",
            name="file_render",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="printjob",
            name="file_stl",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="printjobfile",
            name="file_3mf",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
