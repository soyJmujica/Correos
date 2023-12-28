from django.urls import path
from . import views

urlpatterns = [
path('addagents/', views.AddAgents, name = 'agregar'),
path('agents/', views.Agents, name = 'agentes'),
]