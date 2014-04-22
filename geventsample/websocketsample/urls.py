# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.views import generic as cbv

from . import views

urlpatterns = patterns(
    '',
    url(
        '^$',
        cbv.TemplateView.as_view(template_name="main.html"),
        name='main'
    ),
    url(
        '^socket\.io',
        views.socketio,
        name='socketio'
    ),
)