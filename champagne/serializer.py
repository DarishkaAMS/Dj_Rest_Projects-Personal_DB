from rest_framework import serializers
from champagne.models import Champagne


class ChampagneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champagne
        fields = '__all__'

