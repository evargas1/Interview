from django.urls import path  
from . import views

app_name = 'projects'
urlpatterns = [
    path('home/', views.project_index, name="project_index"),
]
