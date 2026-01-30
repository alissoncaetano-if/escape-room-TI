from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.dashboard, name='dashboard'),
    path('controle/', views.control_room, name='control_room'), # Nova rota da história
    path('cadastro/', views.register, name='register'),
    path('certificado/', views.victory, name='victory'),
]