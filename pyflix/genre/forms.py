from django import forms
from .models import Genre


class GenreForm(forms.Form):

    class Meta:
        model = Genre
        fields = '__all__'
