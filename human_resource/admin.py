from django.contrib import admin
from accounts.models import Employee
from .models_worktime import WorkCode
from .models_worktime import WorkTime

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('code','account','first_name','middle_name','last_name')
	list_filter = ('first_name','last_name')
	ordering = ['code']
	search_fields = ('code','first_name','last_name')

class WorkCodeAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('id','code','description')
	list_filter = ('code','description')
	ordering = ['id']
	search_fields = ('code','description')

class WorkTimeAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('date','employee','project','work_code','start_time','end_time')
	list_filter = ('date','employee','project','work_code')
	ordering = ['-date']
	search_fields = ('date','employee','project','work_code')
	
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WorkCode, WorkCodeAdmin)
admin.site.register(WorkTime, WorkTimeAdmin)