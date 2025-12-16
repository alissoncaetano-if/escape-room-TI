from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.register, name='register'),
    path('certificado/', views.victory, name='victory'),
]