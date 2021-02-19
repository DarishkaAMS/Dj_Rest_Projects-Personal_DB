from django.shortcuts import render
from rest_framework import generics
from champagne.serializer import ChampagneDetailSerializer


class ChampagneCreateView(generics.CreateAPIView):
    serializer_class = ChampagneDetailSerializer
