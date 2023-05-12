from django.shortcuts import render
from .forms import AddFilmForm, AddDirectorForm, CommentForm, RatingForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def homepage(request):
    films = Film.objects.all()
    comments_forms = [CommentForm(initial={'film': film, 'author': request.user}) for film in films]
    rating_forms = [RatingForm(initial={'film': film, 'user': request.user}) for film in films]
    comments = [film.comments.all() for film in films]
    ratings = [film.ratings.all() for film in films]

    films_comments = zip(films, comments_forms, comments, rating_forms, ratings)
    context = {
        'films_comments': films_comments,
        'films': films,
    }
    return render(request, 'homepage.html', context)

class addFilm(CreateView):
    template_name = 'film/addFilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('addFilm')

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

def sfd(request):    
    return render(request, 'film/sfd.html')

class FilmDeleteView(DeleteView):
    template_name = 'film/film_delete.html'
    model = Film
    success_url = reverse_lazy('sfd')

def sdd(request):    
    return render(request, 'director/sdd.html')

class DirectorDeleteView(DeleteView):
    template_name = 'director/director_delete.html'
    model = Director
    success_url = reverse_lazy('sdd')

class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'homepage.html'
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.film_id = self.kwargs['pk']
        print(self.kwargs)
        return super(CommentCreateView, self).form_valid(form)
    

class RatingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'homepage.html'
    model = Rating
    form_class = RatingForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.film_id = self.kwargs['pk']
        print(self.kwargs)
        return super(RatingCreateView, self).form_valid(form)
