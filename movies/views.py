from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie


menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить фильм', 'url_name': 'add_movie'}
]

def index(request):
    movies = Movie.objects.all()
    context = {
        'menu': menu, 
        'movies': movies, 
        'title': 'Главная страница'
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {'menu': menu, 'title': 'О сайте'})


def add_movie(request):
    return HttpResponse('Добавление фильма')

def show_movie(request, post_id):
    return HttpResponse(f'Страница фильма с ID = {post_id}')

def pageNotFound(request, exeption):
    return HttpResponseNotFound('Страницу ещё не отсняли')