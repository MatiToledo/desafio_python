from django.urls import path

from chat import views

app_name='chat'

urlpatterns = [
    path('', views.index, name='Index'),
    path('<str:username>', views.chat, name='Room'),
]
