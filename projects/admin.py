from django.contrib import admin
from .models import ProjectType, ProjectStatus, Project

# Register your models here.
class ProjectTypeAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('code','description')
	list_filter = ('code','description')
	ordering = ['code']
	search_fields = ('code','description')

class ProjectStatusAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('status','description')
	list_filter = ('status','description')
	ordering = ['status']
	search_fields = ('status','description')
	
class ProjectAdmin(admin.ModelAdmin): #Refer DjangoByExample.pdf
	list_display = ('code','type','title','description','status',
					'requester','task_manager','task_leader','estimate','worked_time',
					'order_date','deadline','start_date','completed_date',
					'person_in_charge_1','person_in_charge_2','person_in_charge_3','person_in_charge_4','person_in_charge_5',
					'tester_1','tester_2','tester_3','tester_4','tester_5')
	list_filter = ('code','type','title')
	ordering = ['-code']
	search_fields = ('code','type','title')
	
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)