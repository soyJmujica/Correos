from django.urls import path
from . import views

urlpatterns = [
path('addagents/', views.AddAgent, name = 'agregar'),
path('agents/', views.Agents, name = 'agentes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)