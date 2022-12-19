# Generated by Django 4.1.4 on 2022-12-18 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_note_datecompleted_alter_note_finaldate'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 18, 23, 3, 53, 847639, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='finalDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 18, 23, 3, 53, 847639, tzinfo=datetime.timezone.utc)),
        ),
    ]
