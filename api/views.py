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

class ResultListView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.filter(habit_practiced_id=self.kwargs["pk"])

class HabitDetails(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitResultSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
