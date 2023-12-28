from django.urls import path
from . import views

urlpatterns = [
path('addagents/', views.AddAgent, name = 'agregar'),
path('agents/', views.Agents, name = 'agentes'),
]