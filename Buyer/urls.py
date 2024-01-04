from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('undercontract/', views.undercontract, name = 'under contract'),
path('transactions/', views.transactions, name = 'transacciones'),
path('transactions/<int:property_id>/', views.details, name = 'detalles'),
path('transactions/<int:property_id>/emails', views.emails, name = '7 correos'),
path('transactions/<int:property_id>/closing/', views.saleclosed, name = "cerrar"),
path('transactions/<int:property_id>/pending/', views.salepending, name = "pendiente"),
path('transactions/<int:property_id>/closed/', views.closed, name = 'cerrado'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)