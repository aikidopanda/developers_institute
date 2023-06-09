from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Category, ToDo
from .forms import ToDoForm

def display_todos(request):
    todos = ToDo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos.html', context)



class Add_Todo(CreateView):
    template_name = 'addtodo.html'
    model = ToDo
    form_class = ToDoForm
    success_url = reverse_lazy('todos')
 

# def add_todo(request):
#     if request.method =='POST':
#         form = ToDoForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             todo_new = ToDo(
#                 title = data['title'],
#                 details = data['details'],
#                 has_been_done = data['has_been_done'],
#                 # date_completion = data['date_completion'],
#                 deadline_date = data['deadline_date'],
#                 category = data['category']
#             )
#             todo_new.save()
#             msg = 'New todo was uploaded'
#         else:
#             msg = 'Somehing went wrong'
#     else:
#         form = ToDoForm()
#         msg = ''
#     context = {
#         'form': form,
#         'msg': msg
#     }
#     return render(request,'addtodo.html',context)




# Create your views here.
