# Generated by Django 5.1.2 on 2024-11-01 22:23

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        (
            "crowdprinter",
            "0008_remove_printjob_finished_printattempt_finished_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="printattempt",
            name="dropped_off",
            field=models.BooleanField(default=True),
        ),
    ]
