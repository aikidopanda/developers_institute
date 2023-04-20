from django.shortcuts import render
import json

# Create your views here.

def families(request):
    family = 4 #Change the animal family to print its information to html file
    f = open('animals.json')
    data = json.load(f)
    list_temp = []
    for i in range(len(data['animals']) - 1):
        if data['animals'][i]['family'] == family:
            list_temp.append(data['animals'][i]['name'])
    for i in range(len(data['families'])):
        if data['families'][i]['id'] == family:
            family_temp = data['families'][i]['name']

    context = {
        'animal_list': list_temp,
        'family_name': family_temp
    }
    f.close()
    return render(request, 'families.html/', context)

def animals(request):
    animal = 2 #Change the animal id to print its information to html file
    f = open('animals.json')
    data = json.load(f)
    family_id = data['animals'][animal]['family']
    context = {
        'animal_name': data['animals'][animal]['name'],
        'animal_legs': data['animals'][animal]['legs'],
        'animal_weight': data['animals'][animal]['weight'],
        'animal_height': data['animals'][animal]['height'],
        'animal_speed': data['animals'][animal]['speed'],
        'animal_family': data['families'][family_id - 1]['name'],
    }
    f.close()
    return render(request, 'animals.html/', context)

# family = 4 #Change the animal family to print its information to html file
# f = open('animals.json')
# data = json.load(f)
# list_temp = []
# for i in range(len(data['animals'])):
#     print(data['animals'][i]['family'], data['animals'][i]['name'])
#     if data['animals'][i]['family'] == family:
#         list_temp.append(data['animals'][i]['name'])