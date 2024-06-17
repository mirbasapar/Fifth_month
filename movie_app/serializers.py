from rest_framework import serializers
from .models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj):
        return obj.movie_set.count()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, product):
        reviews = product.reviews.all()
        if reviews:
            sum_reviews = sum(i.stars for i in reviews)
            average = sum_reviews / len(reviews)
            return average
        return None

    class Meta:
        model = Movie
        fields = 'title description duration director reviews average_rating'.split()
