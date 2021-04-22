from rest_framework import serializers
from .models import  Subcripcion

class SubcripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcripcion
        fields = ['nombre', 'descripcion', 'moneda', 'monto', 'creado', 'actualizado']