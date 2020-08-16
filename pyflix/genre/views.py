from django.shortcuts import render
from . import forms

# Create your views here.


def register(request):
    form = forms.GenreForm()
    data_dict = dict(form=form)
    return render(request, 'genre/register.html', data_dict)

