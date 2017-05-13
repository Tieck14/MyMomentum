# -*- coding: utf-8 -*-
"""
Created on Fri May 12 06:43:08 2017

@author: kkt
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^MyMomentum/', include('MyMomentumApp.urls')),
    url(r'^admin/', admin.site.urls),
]