from django.urls import path, include
from .views import MovieListAV, MovieDetailAV, ReviewDetail, ReviewList, StreamPlatformListAV,StreamPlatformDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform-detail'),
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
