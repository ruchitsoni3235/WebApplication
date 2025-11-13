from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # This Page displaying task list
    path('complete/<int:task_id>/', views.complete_task, name='completed_tasks'),
    path('home/', views.home, name='home'),  # displaying radar chart
]

