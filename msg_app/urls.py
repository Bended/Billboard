from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^messages/', views.messages, name='messages'),

   # url(r'^new_msg/', views.MessageForm, name='new_msg'),
]