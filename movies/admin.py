from django.contrib import admin

# Register your models here.
from .models import Actor, Movie, Category, MovieShots, Star, Rating, Reviews, Genre

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(MovieShots)
admin.site.register(Star)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Genre)
