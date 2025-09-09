from django.urls import path, include
from .views import MovieListAV, MovieDetailAV, ReviewDetail, ReviewList, StreamPlatformVS,StreamPlatformDetailAV,ReviewCreate
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
    # path('stream/', StreamPlatformListAV.as_view(), name='platform-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform-detail'),
    path('', include(router.urls)),
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
]
