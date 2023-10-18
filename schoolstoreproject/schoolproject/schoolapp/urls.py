from django.urls import path
from . import views
app_name = 'schoolapp'

urlpatterns = [

    path('', views.demo, name='demo'),
   # path('department_list', views.department_list, name='department_list'),

]