from django.shortcuts import render
from rest_framework import generics
from champagne.serializer import ChampagneDetailSerializer
from champagne.models import Champagne


class ChampagneCreateView(generics.CreateAPIView):
    serializer_class = ChampagneDetailSerializer

class ChampagneListView(generics.ListAPIView):
    serializer_class =
    queryset = Champagne.objects.all()