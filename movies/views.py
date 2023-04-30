from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Movie, Category, Actor


class MoviesListView(ListView):
    """Список постов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Описание фильма"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent', None))
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())


class ActorDetailView(DetailView):
    """Описание режисера"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'
