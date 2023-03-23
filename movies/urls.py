from django.urls import path
from .views import MoviesView, DetailView

urlpatterns = [
    path('', MoviesView.as_view()),
    path('<slug:slug>', DetailView.as_view(), name='movie_detail')
]