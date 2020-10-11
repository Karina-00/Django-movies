from django.forms import ModelForm
from .models import Film, AdditionalInfo, Review


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'premiere', 'year', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ["duration", "genre"]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["stars", "review"]




