"""
URL configuration for audio_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main.views import audio_test, choose_audio , serve_audio


urlpatterns = [
    path('', choose_audio, name='choose_audio'),
    path('audio_test/<int:pk>/', audio_test, name='audio_test'),
    path('serve_audio/<path:filename>', serve_audio, name='serve_audio'),
    path('admin/', admin.site.urls),
]