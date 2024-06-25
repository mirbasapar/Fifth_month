from django.urls import path
from . import views


urlpatterns = [

    path('', views.movie_list_api_view),
    path('<int:id>/', views.movie_detail_api_view),

    path('api/v1/movies/reviews', views.movie_reviews_list_api_view),
    path('api/v1/directors/', views.director_list_api_view),
    path('api/v1/directors/<int:id>', views.director_detail_api_view),

    path('api/v1/reviews/', views.review_list_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
]