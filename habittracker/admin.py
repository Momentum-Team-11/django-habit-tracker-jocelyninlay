from django.contrib import admin
from .models import User, Habit, Result

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Result)

# Register your models here.
