from django.shortcuts import render

# Create your views here.
from .models import  Subcripcion
from .serializers import SubcripcionSerializer
from rest_framework import generics

class SubcripcionList(generics.ListCreateAPIView):
    queryset = Subcripcion.objects.all()
    serializer_class = SubcripcionSerializer

class SubcripcionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcripcion.objects.all()
    serializer_class = SubcripcionSerializer 