from django.shortcuts import render
from .models import Gif_Model, Category
from .forms import GifForm, CategoryForm, LikeForm
from datetime import datetime

# Create your views here.

def homepage_view(request):
    all_gifs = Gif_Model.objects.all().order_by('title')
    like_forms = [LikeForm(initial = {'gif': gif_instance, 'like': True}) for gif_instance in all_gifs]
    dislike_forms = [LikeForm(initial = {'gif': gif_instance, 'like': False}) for gif_instance in all_gifs]

    if request.method == 'POST':
        likeform_submitted = LikeForm(request.POST)
        if likeform_submitted.is_valid():

            gif = likeform_submitted.cleaned_data['gif']
            like = likeform_submitted.cleaned_data['like']

            if like:
                gif.likes += 1
            else:
                gif.likes -= 1

            gif.save()

    gifs_forms = list(zip(all_gifs, like_forms, dislike_forms))

    context = {
        'all_gifs': all_gifs,
        'gifs_forms': gifs_forms
    }
    return render(request, 'homepage.html', context)

def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_gif = Gif_Model(uploader_name = data['uploader_name'], title = data['title'], url = data['url'], created_at = datetime.now())
            # dont know yet how to assign the category dynamically, think of it later
            new_gif.save()
            for i in range(len(data['categories'])):
                cat = Category.objects.get(name = data['categories'][i])
                cat.gifs.add(new_gif)
            msg = 'New gif is uploaded!'
            
        else:
            msg = 'Something went wrong'
    else:
        form = GifForm()
        msg = ''
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'addgif.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_cat = Category(name = data['name'])
            new_cat.save()
            msg = 'New gif is uploaded!'
        else:
            msg = 'Something went wrong'
    else:
        form = CategoryForm()
        msg = ''
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'addcategory.html', context)

def gif_view(request, id):
    all_gifs = Gif_Model.objects.all()
    context = {
        'all_gifs': all_gifs,
        'id': id
    }
    return render(request, 'gifview.html', context)

def categories_view(request):
    all_cats = Category.objects.all()
    context = {
        'all_cats': all_cats
    }
    return render(request, 'categoriesview.html',context)

def category_view(request, cat_id):
    category = Category.objects.get(id = cat_id)
    all_gifs = Gif_Model.objects.all()
    list_temp = []
    for gif in category.gifs.all():
        list_temp.append(gif)
    context = {
        'gifs_list': list_temp,
        # 'all_gifs': all_gifs,
        'category': category.gifs.all()
        # 'cat_id': cat_id
    }
    return render(request, 'categoryview.html', context)
    



