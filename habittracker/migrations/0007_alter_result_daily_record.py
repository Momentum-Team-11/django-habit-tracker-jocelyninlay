# Generated by Django 4.0.3 on 2022-03-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0006_alter_result_date_accomplished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='daily_record',
            field=models.CharField(max_length=200),
        ),
    ]
