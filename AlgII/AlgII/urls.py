from django.conf.urls import url
# from django.urls import path, include, reverse
from django.shortcuts import redirect
from django.contrib import admin
from . import views
import sys
sys.path.append(".")

from ..Core.viewsets import CalculoViewSet


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^result/', views.result),
    url(r'^chewie/', views.chewie),
    url(r'^api/calculadora/', core_viewsets.CalculoViewSet),
    url(r'^$', views.homepage)
]
