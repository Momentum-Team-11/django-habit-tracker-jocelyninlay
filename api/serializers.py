from habittracker.models import Habit, Result, User
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "overall_goal",
        )
class HabitNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "name",
        )

class ResultSerializer(serializers.ModelSerializer):
   habit_practiced = serializers.SlugRelatedField(read_only=True, slug_field='name')
   class Meta:
        model = Result
        fields = (
        "habit_practiced",
        "daily_record",
        "date_accomplished",
        )

class HabitResultSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True, required=False)
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "results",
        )

class UserSerializer(serializers.ModelSerializer):
    habits = serializers.PrimaryKeyRelatedField(many=True, queryset=Habit.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'habits')
