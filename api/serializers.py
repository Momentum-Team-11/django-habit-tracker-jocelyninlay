from habittracker.models import Habit, Result
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "overall_goal",
            "app_user",
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
        "pk",
        
        )