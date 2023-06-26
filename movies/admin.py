from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Actor, Movie, Category, MovieShots, Star, Rating, Reviews, Genre

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
    list_display_links = ('name',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ('name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


class ReviewsInLines(admin.TabularInline):
    """Отзывы к фильму в админке"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="125" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ('name', 'category', 'url', 'draft')
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    readonly_fields = ('get_image',)
    inlines = [MovieShotsInLine, ReviewsInLines]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    fieldsets = (
        (None, {
            'fields': (('name', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image')),
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ("Actors", {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genre', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_USA', 'fees_in_world'),)
        }),
        ("Options", {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="120" height="170"')

    get_image.short_description = "Изображение"

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была изменина"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была изменина"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)

    unpublish.short_description = 'Убрать с публикации'
    unpublish.allowed_permissions = ('change',)

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('name', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"')

    get_image.short_description = "Постер"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('star', 'movie', 'ip')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жнары"""
    list_display = ('name', 'url')


admin.site.register(Star)


admin.site.site_title = 'Djagno Movie'
admin.site.site_header = 'Django Movie'
