from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gen_resume/', views.gen_resume, name='gen_resume'),
    path('resume_detail/', views.resume_detail, name='resume_detail'),
]