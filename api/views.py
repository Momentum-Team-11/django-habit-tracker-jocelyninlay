from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from habittracker.models import Habit, Result
from .serializers import HabitSerializer, ResultSerializer
from rest_framework.generics import ListAPIView

class HabitListView(APIView):
    
    
    def get(self, request, format=None):
    
    #queryset:
        habits = Habit.objects.all()
    #serializer:
        HabitSerializer(habits, many=True)

    #permissions if you didnt do the global aone
    #return a response with jsondata. the end goal is to take in a __, do what its asking, and return a response.
        return Response(serializer.data)

class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class ResultListView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
