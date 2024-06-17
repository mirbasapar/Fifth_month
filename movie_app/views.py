from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializer
from .models import Director, Movie, Review
from django.db.models import Avg


@api_view(['GET'])
def director_list_api_view(request):

    data = Director.objects.all()

    list_ = DirectorSerializer(data, many=True).data

    return Response(data=list_)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)

    except Director.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = DirectorSerializer(director).data

    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    data = Movie.objects.all()

    list_ = MovieSerializer(data, many=True).data

    return Response(data=list_)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = MovieSerializer(movie).data

    return Response(data=data)


@api_view(['GET'])
def movie_reviews_list_api_view(request):
    data = Movie.objects.all()

    list_ = MovieReviewsSerializer(data, many=True).data

    return Response(data=list_)

@api_view(['GET'])
def review_list_api_view(request):
    data = Review.objects.all()

    list_ = ReviewSerializer(data, many=True).data

    return Response(data=list_)


# def calculate_average_rating():
#     return Review.objects.aggregate(Avg('stars'))['stars__avg']


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)

    except Review.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = ReviewSerializer(review).data

    return Response(data=data)


