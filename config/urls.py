"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from habittracker import views as habittracker_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", habittracker_views.home, name="home"),
    path('accounts/', include('registration.backends.simple.urls')),
    path("habit", habittracker_views.habit_list, name="habit_list"),
    path("habit/add/", habittracker_views.add_habit, name="add_habit"),
    path("habit/<int:pk>/add/", habittracker_views.add_result, name="add_result"),
    path("habit/<int:pk>/", habittracker_views.habit_details,  name="habit_details"),
    path("habit/<int:year>/<int:month>/<int:day>/", habittracker_views.date_details,  name="date_details"),
    path("habit/<int:pk>/edit/", habittracker_views.edit_habit, name="edit_habit"),
    path("habit/<int:pk>/edit/", habittracker_views.edit_result, name="edit_result"),
    path("habit/<int:pk>/delete/", habittracker_views.delete_habit, name="delete_habit"),
]
