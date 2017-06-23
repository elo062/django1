# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Je fais un include des urls du blog

urlpatterns = [
   url(r'^blog/', include('blog.urls')),
]
