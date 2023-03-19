from django.db import models
from datetime import date


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категории", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер и режисер"
        verbose_name_plural = "Актеры и режисеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """Фильмы"""
    name = models.CharField('Имя', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)
    country = models.CharField(max_length=150)
    directors = models.ManyToManyField(Actor, verbose_name='Режисеры', related_name='film_directors')
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actors")
    genre = models.ManyToManyField(Genre, verbose_name="Жанры")
    year = models.PositiveSmallIntegerField('Год выпуска' , default=2023)
    fees_in_USA = models.PositiveIntegerField('Сборы в США', default=0)
    fees_in_world = models.PositiveIntegerField('Сборы в мире', default=0)
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.SET_NULL, null=True)
    budget = models.PositiveIntegerField('Бюджет', default=0)
    poster = models.ImageField('Изображение', upload_to='movie/')
    tagline = models.CharField('Слоган', max_length=150, default='')
    draft = models.BooleanField('Черновик', default=False)
    world_premiere = models.DateField('Примьера в мире', default=date.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class MovieShots(models.Model):
    """Кадры из фильма"""
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class Star(models.Model):
    """Звезда рейтинга"""
    value = models.IntegerField("Значение")

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Здвезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адресс', max_length=15)
    star = models.ForeignKey(Star, verbose_name='Звезда', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=150)
    text = models.TextField('Текст', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'