from django.contrib import admin
from .models import Genre, Movie, Director


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'rating', 'is_published', 'director')
    list_filter = ('is_published', 'genres', 'release_year')
    search_fields = ('title', 'description')

# то, что админу нельзя изменить
    readonly_fields = ('time_create', 'time_update')

# В странице админа разделяем информацию на подкатегории, fields - встроенное название
    fieldsets = (
        ('Основная информация',{
            'fields': ('title', 'description', 'poster')
        }),
        ('Данные о релизе', {
            'fields': (('release_year', 'rating'),) 
            # ((___),) -в строку соединяет маленькие элементы
        }),
        ('Связи', {
            'fields': ('director', 'genres')
        }),
        ('Статус', {
            'classes': ('collapse',),
            # позволяет сворачивать подкатегорию
            'fields': ('is_published', 'time_create', 'time_update')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass