from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import UniqueConstraint

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Habit(models.Model):
    name = models.CharField(max_length=200)
    overall_goal = models.IntegerField()
    description = models.TextField(max_length=1000)
    app_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="goal_setter")
    

    def __str__(self):
        return self.overall_goal

class Result(models.Model):
    habit_practiced = models.ForeignKey(Habit, on_delete=models.CASCADE, null=True, blank=True, related_name="habit_practiced")
    daily_record = models.IntegerField() 
    date_accomplished = models.DateField(auto_now_add=datetime.now, verbose_name="Date for habit")

    def __str__(self):
        return str(self.daily_record)
     
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["habit_practiced", "date_accomplished"], name="one_record_per_day")
        ]