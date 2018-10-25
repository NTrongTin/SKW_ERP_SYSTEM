from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from accounts.models import Employee
from django.utils.timezone import datetime #important if using timezones

class CurrentMonthWorkTimeManager(models.Manager):
    def get_queryset(self):
        today = datetime.today()
        return super(CurrentMonthWorkTimeManager,self).get_queryset().filter(date__month=today.month)

class WorkCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description
		
class WorkTime(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='all_work_time_records')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='project_work_time')
    work_code = models.ForeignKey(WorkCode, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    current_month_work_time = CurrentMonthWorkTimeManager() # Our custom manager
