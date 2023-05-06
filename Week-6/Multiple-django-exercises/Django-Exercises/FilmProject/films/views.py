from django.shortcuts import render
from .forms import AddFilmForm, AddDirectorForm
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def homepage(request):
    films = Film.objects.all()
    context = {
        'films': films,
    }
    return render(request, 'homepage.html', context)

class addFilm(CreateView):
    template_name = 'film/addFilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('addFilm')


# def addFilm(request):
#     msg = ''
#     if request.method == 'POST':
#         form = AddFilmForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_film = Film(
#                 title = data['title'],
#                 release_date = data['release_date'],
#                 created_in_country = data['created_in_country'],
#                 available_in_countries = data['available_in_countries'],
#                 category = data['category'],
#                 director = data['director'],
#             )
#             new_film.save()
#         else:
#             errors = form.errors()
#             msg = "Error"
#     else:
#         form = AddFilmForm()
#     context = {
#         'form': form,
#         'msg': msg
#     }
#     return render(request,'film/addFilm.html',context)

def addDirector(request):
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_director = Director(
                first_name= data['first_name'],
                last_name = data['last_name']
            )
            new_director.save()
        else:
            errors = form.errors()
            print(errors)
    else:
        form = AddDirectorForm()
    context = {
        'form': form
    }
    return render(request,'directors/addDirector.html',context)
