from ..models import Category, Movie
from django import template


register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': movies}