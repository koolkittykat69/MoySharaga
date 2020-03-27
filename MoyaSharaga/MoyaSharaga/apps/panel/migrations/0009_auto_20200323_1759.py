# Generated by Django 3.0.4 on 2020-03-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_timetable_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_datetime_start',
            field=models.TimeField(verbose_name='Время начала пары'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_datetime_stop',
            field=models.TimeField(verbose_name='Время конца пары'),
        ),
    ]