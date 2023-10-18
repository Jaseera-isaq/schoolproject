from django.urls import path
from . import views
app_name = 'credentials'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('register/login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('buttonclick', views.buttonclick, name='buttonclick'),
    path('newform', views.newform, name='newform'),
    path('register/newform', views.newform, name='newform'),
    path('submit', views.submit, name='submit'),
    path('register/submit', views.submit, name='submit'),

 ]