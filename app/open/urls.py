# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import include, url

from .views import openAccountReal, openAccountDemo, openAccountAnonymous

urlpatterns = [
    url(r'^demo', openAccountDemo,  name='Demo'),
    url(r'^real', openAccountReal,  name='Real'),
    url(r'^Anonymous', openAccountAnonymous,  name='Anonymous'),
]
