from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    
    url(r'^displogin', views.dispLogin, name='dispLogin'),
    url(r'^login_user/', views.login_user, name='login_user'),
    url(r'^register_displ/', views.register_displ, name='register_displ'),
    url(r'^register/', views.register, name='register'),
    url(r'^messages/', views.messages, name='messages'),
    url(r'^logout/', views.logout_user, name='logout_user'),
    url(r'^new_msg/', views.new_msg, name='new_msg'),
    url(r'^trash/', views.trash, name='trash'),
    url(r'^$', views.home, name='home'),
]