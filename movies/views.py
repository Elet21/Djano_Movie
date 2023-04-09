from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie


class MoviesListView(ListView):
    """Список постов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Описание фильма"""
    model = Movie
    slug_field = "url"
