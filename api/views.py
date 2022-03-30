from rest_framework.views import APIView
from rest_framework.response import Response
from habittracker.models import Habit, Result, User
from .serializers import HabitSerializer, ResultSerializer, UserSerializer, HabitResultSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, CreateAPIView


class HabitListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView ):
    #queryset:
    queryset = Habit.objects.all()
    #serializer:
    serializer_class = HabitSerializer
    
    def perform_create(self, serializer):
        serializer.save(app_user=self.request.user)

class ResultListView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class HabitDetails(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitResultSerializer

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
