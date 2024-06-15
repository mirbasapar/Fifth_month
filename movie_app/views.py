from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializers, MovieSerializers, ReviewSerializers
from .models import Director, Movie, Review


@api_view(['GET'])
def director_list_api_view(request):

    data = Director.objects.all()

    list_ = DirectorSerializers(data, many=True).data

    return Response(data=list_)


@api_view(['GET'])
def director_detail_api_view(request):
    try:
        product = Director.objects.get(id=id)

    except Director.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = DirectorSerializers(product).data

    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    data = Movie.objects.all()

    list_ = MovieSerializers(data, many=True).data

    return Response(data=list_)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        product = Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = MovieSerializers(product).data

    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    data = Review.objects.all()

    list_ = ReviewSerializers(data, many=True).data


    return Response(data=list_)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        product = Review.objects.get(id=id)

    except Review.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = ReviewSerializers(product).data

    return Response(data=data)
