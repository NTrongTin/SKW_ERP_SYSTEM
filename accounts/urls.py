from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


urlpatterns = [
#    url(r'^signup/$', accounts_views.signup, name='signup'),
#    url(r'^login/$', views.user_login, name='login'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
#    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
