"""
URL configuration for missao_tech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rotas de login/logout nativas
    path('accounts/', include('django.contrib.auth.urls')), 

    #Rota raiz e vitórias ficam no Core
    path('', include('apps.core.urls')),

    path('sala/hardware/', include('apps.hardware.urls')),
    path('sala/word/', include('apps.word.urls')),
    path('sala/excel/', include('apps.excel.urls')),
]
