from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('resume/', views.resume, name='resume')
]
