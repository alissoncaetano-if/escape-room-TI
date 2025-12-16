from django.urls import path
from . import views

app_name = 'excel'

urlpatterns = [
    path('', views.room, name='room')
]