from django.shortcuts import render
from rest_framework import generics
from champagne.serializer import ChampagneDetailSerializer, ChampagneListSerializer
from champagne.models import Champagne


class ChampagneListView(generics.ListAPIView):
    serializer_class = ChampagneListSerializer
    queryset = Champagne.objects.all()


class ChampagneCreateView(generics.CreateAPIView):
    serializer_class = ChampagneDetailSerializer


class ChampagneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChampagneDetailSerializer
    queryset = Champagne.objects.all()
    permission_classes = ...


