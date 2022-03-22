from django import forms
from .models import User, Habit, Result

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["overall_goal", "description"]

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["habit_practiced", "daily_record", "goal_accomplished"]