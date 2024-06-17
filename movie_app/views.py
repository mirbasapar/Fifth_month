from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializer
from .models import Director, Movie, Review


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        data = Director.objects.all()

        list_ = DirectorSerializer(data, many=True).data

        return Response(data=list_)
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.object.create(
            name=name,
        )
        director.save()

        return Response(data={'director_id': director.id, 'name': director.name},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)

    except Director.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        data = Movie.objects.all()

        list_ = MovieSerializer(data, many=True).data

        return Response(data=list_)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.object.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )
        movie.save()
        return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_reviews_list_api_view(request):
    data = Movie.objects.all()

    list_ = MovieReviewsSerializer(data, many=True).data

    return Response(data=list_)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        data = Review.objects.all()

        list_ = ReviewSerializer(data, many=True).data

        return Response(data=list_)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.object.creare(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        review.save()

        return Response(data={'movie_id': movie_id, 'text': review.text, 'stars': review.stars},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)

    except Review.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

