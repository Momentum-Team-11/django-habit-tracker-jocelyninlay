# Generated by Django 4.0.3 on 2022-03-22 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0002_rename_daily_goal_habit_overall_goal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='habit_performed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit_performed', to='habittracker.habit'),
        ),
        migrations.AlterField(
            model_name='result',
            name='daily_record',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
