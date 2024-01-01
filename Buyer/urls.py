from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('undercontract/', views.undercontract, name = 'under contract'),
path('transactions/', views.transactions, name = 'transacciones'),
path('transactions/<int:property_id>/', views.details, name = 'detalles'),
path('transactions/<int:property_id>/emails', views.emails, name = '7 correos')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)