from django.shortcuts import render
from .models_worktime import WorkTime

def work_time(request):
    current_month_work_time = WorkTime.current_month_work_time.all()
    return render(request, 'human_resource/worktime.html', {'current_month_work_time':current_month_work_time})