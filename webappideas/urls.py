"""webappideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from socialauth import views as social_auth_views
from ideas import urls as ideas_urls
from .views import HomeView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("ideas/", include('ideas.urls')),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", social_auth_views.login, name="login"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", HomeView.as_view(), name="home"),
]
