from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models

class CalculoViewSet(viewsets.ModelViewSet):
    queryset = models.Calculo.objects.all()
    serializer_class = serializers.CalculoSerializer