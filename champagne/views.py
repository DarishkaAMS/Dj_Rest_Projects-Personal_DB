from django.shortcuts import render
from rest_framework import generics


class ChampagneCreateView(generics.CreateAPIView):
    serializer_class = ...
