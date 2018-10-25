from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^worktime/$', views.work_time, name='work_time'),
]