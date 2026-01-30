from django.urls import path
from . import views

app_name = 'hardware'

urlpatterns = [
    path('loja/', views.store, name='store'), # Nova rota da Loja
    path('lab/', views.room, name='room'),    # Rota do Lab (Montagem)
]