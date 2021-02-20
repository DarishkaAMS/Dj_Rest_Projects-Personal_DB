from rest_framework import serializers
from champagne.models import Champagne


class ChampagneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champagne
        fields = ('id', 'brand', 'champ_type')


class ChampagneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champagne
        fields = '__all__'

