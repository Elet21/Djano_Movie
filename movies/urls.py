from django.urls import path
from .views import MoviesListView, MovieDetailView

urlpatterns = [
    path('', MoviesListView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail')
]