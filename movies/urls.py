from django.urls import path
from .views import MoviesListView, MovieDetailView, AddReview, ActorDetailView

urlpatterns = [
    path('', MoviesListView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review_url'),
    path('actor/<str:slug>/', ActorDetailView.as_view(), name='actor_detail_url'),
]