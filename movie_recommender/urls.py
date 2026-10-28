"""movie_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('userHome/', views.userHome, name='userHome'),
    path('camera/', views.camera, name='camera'),
    path('movies/surprise/', views.moviesSurprise, name='moviesSurprise'),
    path('movies/angry/', views.moviesAngry, name='moviesAngry'),
    path('movies/sad/', views.moviesSad, name='moviesSad'),
    path('movies/disgust/', views.moviesDisgust, name='moviesDisgust'),
    path('movies/happy/', views.moviesHappy, name='moviesHappy'),
    path('movies/fear/', views.moviesFear, name='moviesFear'),
    path('movies/neutral/', views.moviesNeutral, name='moviesNeutral'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('add_movie_view/', views.add_movie_view, name='add_movie_view'),
    path('view_movies/', views.view_movies, name='view_movies'),
    path('delete_movie/', views.delete_movie, name='delete_movie'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('admin_view_feedback/', views.admin_view_feedback, name='admin_view_feedback'),
]