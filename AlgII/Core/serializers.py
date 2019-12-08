from rest_framework import serializers
from .models import Calculo

class CalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculo
        fields = ('matriz','determinante', 'traco', 'inversa', 'polinomio_caracteristico', 'autovalores', 'autovetores', 'matriz_diagonal')