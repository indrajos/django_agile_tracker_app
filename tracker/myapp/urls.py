from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('stories/', views.story_list, name='story_list'),
    path('stories/<int:id>/', views.task_list, name='task_list'),
    path('stories/create/', views.create_story, name='create_story'),
    path('stories/<int:id>/create_task/', views.create_task, name='create_task'),
    path('tasks/create_time_entry/<int:id>/', views.create_time_entry, name='create_time_entry'),
    path('tasks/<int:id>/time_entries/', views.time_entry_list, name='time_entry_list')
]