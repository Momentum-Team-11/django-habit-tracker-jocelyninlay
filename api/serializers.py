from habittracker.models import Habit, Result, User
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "overall_goal",
            "app_user",
            "owner",
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
        "pk",
        "habit_practiced",
        "daily_record",
        "date_accomplished",
        )


class UserSerializer(serializers.ModelSerializer):
    habits = serializers.PrimaryKeyRelatedField(many=True, queryset=Habit.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'habits')
