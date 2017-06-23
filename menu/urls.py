# -*- coding: utf-8 -*-
"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

from blog import views

urlpatterns = [
    url(r'^accueil$', views.home), # Accueil du blog
    url(r'^article/(\d+)$', views.view_article),  # Vue d'un article
]

# Nous commençons par un exemple avec une vue qui renvoie juste la date actuelle à l'utilisateur, et son fichierurls.pyassocié :
from django.conf.urls import url
from . import views

urlspatterns = [
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]
