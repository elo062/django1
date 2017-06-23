# -*- coding: utf-8 -*-

# Nous commençons par un exemple avec une vue qui renvoie juste la date actuelle à l'utilisateur, et son fichierurls.pyassocié :
from django.conf.urls import url
from . import views

urlspatterns = [
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]
