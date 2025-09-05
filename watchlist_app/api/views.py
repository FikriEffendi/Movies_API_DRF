from watchlist_app.api import serializers
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamPlatform,Review
from rest_framework import status
from rest_framework import generics

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class StreamPlatformListAV(APIView):
    def get(self,request):
        platforms=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platforms,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            Response(serializer.errors)

class MovieListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
