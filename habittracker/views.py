from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Result
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, ResultForm
import datetime


def home(request):
    if request.user.is_authenticated:
        return redirect("habit_list")
    return render(request,"home.html")

@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habit_list.html", {"habits": habits})

@login_required
# def date_details(request, pk, year=None, month=None, day=None):
#     habit = get_object_or_404(Habit, pk=pk)
#     results = Result.objects.filter(habit_practiced=habit.id)
#     if year is None:
#         date_for_habit = datetime.date.today
#     else:
#         date_for_habit = datetime.date(year, month, day)
#     return render (request, "habit_details.html", {"habit": habit, "results": results})


def habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    results = Result.objects.filter(habit_practiced=habit.id)
    return render (request, "habit_details.html", {"habit": habit, "results": results})

def date_details(request, year=None, month=None, day=None):
    if year is None:
        date_for_habit = datetime.date.today
    else:
        date_for_habit = datetime.date(year, month, day)
    next_day = date_for_habit + datetime.timedelta(days=1)
    prev_day = date_for_habit + datetime.timedelta(days=-1)
    habit, _ = request.user.app_user.get_or_create(date=date_for_habit)
    result = Result.objects.for_user(request.user).exclude(pk__in=[r.pk for r in result.habit_practiced.all()])

    return render(
        request,
        "date_details.html",
        {
            "habit": habit,
            "result": result,
            "date": date_for_habit,
            "next_day": next_day,
            "prev_day": prev_day,
        },
    )

@login_required
def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="habit_list")
    return render(request, "add_habit.html", {"form": form})

@login_required
def add_result(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = ResultForm()
    else:
        form = ResultForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="habit_list")
    return render(request, "add_result.html", {"form": form, "habit": habit})

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to="habit_list")
    return render(request, "edit_habit.html", {"form": form, "habit": habit})

def edit_result(request, pk):
    result = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=result)
    else:
        form = HabitForm(data=request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect(to="habit_list")
    return render(request, "edit_result.html", {"form": form, "habit": habit, "result": result})

def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method =="POST":
        habit.delete()
        return redirect(to="habit_list")
    return render(request, "delete_habit.html", {"habit": habit})

def delete_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method =="POST":
        result.delete()
        return redirect(to="habit_list")
    return render (request, "delete_habit.html", {"result": result})