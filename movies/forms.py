from django import forms

from .models import Reviews, Rating, Star


class ReviewForm(forms.ModelForm):
    """Форма отхывов"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    """Форма рейтинга"""

    star = forms.ModelChoiceField(queryset=Star.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ('star',)
