from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import NameForm, PhoneForm

# Create your views here.

# def search_phone(request):
#     context = {}
#     return render(request, 'searchphone.html', context)

def get_by_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            if Person.objects.filter(name = form.cleaned_data['search_name']):
                person = Person.objects.filter(name = form.cleaned_data['search_name'])
                result = person.values()
            else:
                result = 'No results'

    else:
        form = NameForm()
        result = ''
    context = {
        "form": form,
        'result': result
    }

    return render(request, "searchbyname.html", context)

def get_by_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            if Person.objects.filter(phone_number = form.cleaned_data['search_phone']):
                person = Person.objects.filter(phone_number = form.cleaned_data['search_phone'])
                result = person.values()
            else:
                result = form.cleaned_data['search_phone']
    else:
        form = PhoneForm()
        result = ''
    context = {
        "form": form,
        'result': result
    }

    return render(request, "searchbyphone.html", context)
