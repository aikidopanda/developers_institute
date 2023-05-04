from django.shortcuts import render
from .forms import AddFilmForm
from .models import *

# Create your views here.

def homepage(request):
    films = Film.objects.all()
    context = {
        'films': films,
    }
    return render(request, 'homepage.html', context)

def addFilm(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_film = Film(
                title = data['title'],
                release_date = data['release_date'],
                created_in_country = data['created_in_country'],
                available_in_countries = data['available_in_countries'],
                category = data['category'],
                director = data['director'],
            )
        else:
            errors = form.errors()
            print(errors)
    else:
        form = AddFilmForm()
    context = {
        'form': form
    }
    return render(request,'film/addFilm.html',context)
