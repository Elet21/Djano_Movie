from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Movie


class MoviesView(View):
    """Список постов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movies_list': movies})


class DetailView(View):
    """Описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})