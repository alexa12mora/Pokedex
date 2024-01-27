# pokedexApp/serializers.py
from rest_framework import serializers

class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    types = serializers.ListField(child=serializers.CharField())
    height = serializers.FloatField()
    weight = serializers.FloatField()
