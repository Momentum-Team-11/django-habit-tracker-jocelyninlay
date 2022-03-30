from rest_framework.views import APIView
from rest_framework.response import Response
from habittracker.models import Habit, Result, User
from .serializers import HabitSerializer, ResultSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView


class HabitListView(ListAPIView):
    #queryset:
    queryset = Habit.objects.all()
    #serializer:
    serializer_class = HabitSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ResultListView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class HabitDetails(RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all(), Result.objects.all()
    serializer_class = HabitSerializer

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
