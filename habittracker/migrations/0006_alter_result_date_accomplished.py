# Generated by Django 4.0.3 on 2022-03-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0005_result_one_record_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date_accomplished',
            field=models.DateField(auto_now_add=True),
        ),
    ]
