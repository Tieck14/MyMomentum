# -*- coding: utf-8 -*-
"""
Created on Fri May 12 06:39:42 2017

@author: kkt
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]