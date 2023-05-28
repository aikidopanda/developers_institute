from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import UpdateForm

# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_create(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-list')
    else:
        serializer = BookSerializer()
    return render(request, 'book_create.html', {'serializer': serializer})

class BookUpdate(CreateView):
    form_class = UpdateForm
    model = Book
    template_name = 'book_update.html'
