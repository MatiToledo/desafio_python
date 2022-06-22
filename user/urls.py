from django.urls import path

from user import views

app_name='user'
urlpatterns = [
   path('register', views.register, name='Register'),
   path('login', views.login_request, name='Login'),
   path('logout', views.logout_request, name='Logout'),
   path('profile', views.user_update, name='Profile'),
   path('profile/avatar', views.avatar_load, name='Avatar'),
]