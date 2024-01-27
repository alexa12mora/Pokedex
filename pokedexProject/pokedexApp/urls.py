# Import necessary modules and classes
from django.urls import path
from .views import PokemonListView,WeightFilteredPokemonView,TypeFilteredPokemonView,HeightAndTypeFilteredPokemonView,ReversedNamePokemonView


# define the urls
urlpatterns = [
    path('pokemon/list/', PokemonListView.as_view(), name='pokemon-list'),
    path('pokemon/list/weight/', WeightFilteredPokemonView.as_view(), name='weight-filtered-pokemon-list'),
    path('pokemon/list/grass/', TypeFilteredPokemonView.as_view(), name='grass-filtered-pokemon-list'),
    path('pokemon/list/flying/', HeightAndTypeFilteredPokemonView.as_view(), name='flying-filtered-pokemon-list'),
    path('pokemon/list/inverded/', ReversedNamePokemonView.as_view(), name='inverded-filtered-pokemon-list'),
]
