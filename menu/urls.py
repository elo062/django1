# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]

# Mettre r'^$'comme URL équivaut à spécifier la racine du site web. Autrement dit, si nous avions utilisé cette URL à la place der'^accueil/$', la vue serait accessible depuishttp://www.crepes-bretonnes.com/.
