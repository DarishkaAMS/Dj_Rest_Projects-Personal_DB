from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from champagne.models import Champagne
from champagne.permisions import IsOwnerOrReadOnly
from champagne.serializer import ChampagneDetailSerializer, ChampagneListSerializer


class ChampagneListView(generics.ListAPIView):
    serializer_class = ChampagneListSerializer
    queryset = Champagne.objects.all()
    permission_classes = (IsAdminUser, )


class ChampagneCreateView(generics.CreateAPIView):
    serializer_class = ChampagneDetailSerializer


class ChampagneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChampagneDetailSerializer
    queryset = Champagne.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


