# Import necessary modules and classes
from .serializer import PokemonSerializer
from concurrent.futures import ThreadPoolExecutor
from rest_framework import exceptions, status, views
from rest_framework.response import Response
from django.core.cache import cache
import requests
from rest_framework.views import APIView

# Define a base class for Pokemon views
class BasePokemonView(views.APIView):
    # Base URL for the Pokeapi
    base_url = 'https://pokeapi.co/api/v2/pokemon'

    # Function to fetch Pokemon data from cache or the Pokeapi
    def fetch_pokemon_data(self, url):
        pokemon_data = cache.get(url)
        if pokemon_data is not None:
            return pokemon_data
        try:
            response = requests.get(url)
            response.raise_for_status()
            pokemon_data = response.json()
            cache.set(url, pokemon_data)

            return pokemon_data
        except requests.exceptions.RequestException as e:
            raise exceptions.APIException(f"Failed to fetch Pokemon data: {str(e)}")

    # Function to get base Pokemon data from the Pokeapi
    def get_base_pokemon_data(self):
        try:
            response = requests.get(f'{self.base_url}?limit=50')
            response.raise_for_status()
            data = response.json().get('results', [])
            
            # Use ThreadPoolExecutor for concurrent fetching of Pokemon data
            with ThreadPoolExecutor() as executor:
                full_data = list(executor.map(self.fetch_pokemon_data, map(lambda pokemon: pokemon['url'], data)))
            return full_data
        except requests.exceptions.RequestException as e:
            raise exceptions.APIException(f"Failed to fetch base Pokemon data: {str(e)}")

    # Function to serialize Pokemon data using a serializer
    def serialize_pokemon_data(self, pokemon_data):
        serializer = PokemonSerializer(pokemon_data)
        return serializer.data
    
    # Filtering functions for different criteria
    def filter_by_weight(self, pokemon, min_weight, max_weight):
        return min_weight <= pokemon['weight'] <= max_weight

    def filter_by_type(self, pokemon, type):
        return type in [t['type']['name'] for t in pokemon['types']]

    def filter_by_height_and_type(self, pokemon, min_height, type):
        return pokemon['height'] > min_height and self.filter_by_type(pokemon, type)

    def reverse_name(self, pokemon):
        pokemon['name'] = pokemon['name'][::-1]
        return pokemon

# Subclass of BasePokemonView for listing Pokemon (50 first)
class PokemonListView(BasePokemonView):
    def get(self, request, *args, **kwargs):
        base_data = self.get_base_pokemon_data()
        filter_func = kwargs.get('filter_func', lambda pokemon: True)
        filtered_data = [pokemon for pokemon in base_data if filter_func(pokemon)]
        serialized_data = [self.serialize_pokemon_data(pokemon) for pokemon in filtered_data]
        return Response(serialized_data, status=status.HTTP_200_OK)

# Subclass of PokemonListView for filtering by weight
class WeightFilteredPokemonView(PokemonListView):
    def get(self, request, *args, **kwargs):
        kwargs['filter_func'] = lambda pokemon: self.filter_by_weight(pokemon, 30, 80)
        return super().get(request, *args, **kwargs)

# Subclass of PokemonListView for filtering by type 'grass'
class TypeFilteredPokemonView(PokemonListView):
    def get(self, request, *args, **kwargs):
        kwargs['filter_func'] = lambda pokemon: self.filter_by_type(pokemon, 'grass')
        return super().get(request, *args, **kwargs)

# Subclass of PokemonListView for filtering by height and type 'flying'
class HeightAndTypeFilteredPokemonView(PokemonListView):
    def get(self, request, *args, **kwargs):
        kwargs['filter_func'] = lambda pokemon: self.filter_by_height_and_type(pokemon, 10, 'flying')
        return super().get(request, *args, **kwargs)

# Subclass of PokemonListView for reversing Pokemon names
class ReversedNamePokemonView(PokemonListView):
    def get(self, request, *args, **kwargs):
        kwargs['filter_func'] = self.reverse_name
        return super().get(request, *args, **kwargs)
