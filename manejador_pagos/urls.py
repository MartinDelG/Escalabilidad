from django.urls import path
from . import views

urlpatterns = [
    path('generarRecibo/<int:id_estudiante>/', views.generar_recibo, name='generar_recibo'),
    path('', views.home, name='home')
]
