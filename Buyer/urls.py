from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('undercontract/', views.undercontract, name = 'under contract'),
path('transactions/', views.transactions, name = 'transacciones')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)