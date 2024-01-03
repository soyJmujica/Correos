from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('', views.index, name = "index"),
path('addagents/', views.AddAgent, name = 'agregar'),
path('agents/', views.Agents, name = 'agentes'),
path('agents/<int:agent_id>/', views.AgentInfo, name = 'detalles agente'),
path('agents/<int:agent_id>/pending/', views.AgentsPending, name = "pendientes"),
path('agents/<int:agent_id>/closed/', views.AgentsClosed, name = "vendidos"),
path('agents/<int:agent_id>/deals/', views.AgentsDeals, name = "pendientes y vendidos")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)