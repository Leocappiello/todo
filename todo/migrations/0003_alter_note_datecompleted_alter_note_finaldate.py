# Generated by Django 4.1.4 on 2022-12-18 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_note_datecompleted_note_finaldate_alter_note_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 12, 18), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='finalDate',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 12, 18)),
        ),
    ]
