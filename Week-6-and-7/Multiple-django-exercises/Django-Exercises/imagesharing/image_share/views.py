from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import SignUpForm, ImageForm
from .models import Image
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(LoginRequiredMixin, DetailView): # LoginRequiredMixin - to access users that already login, DetailView - we need to see only about 1 user
    model = User #python bull-in model
    template_name = 'profile.html'
    context_object_name = 'user' # take object to template

    def get_object(self, queryset=None): # take loggedin user
        pk = self.kwargs.get('pk') # take user by id
        return self.request.user #self.query.set - access to user
    
@login_required
def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('profile')
    else:
        form = ImageForm()
    context = {
        'form': form
    }
    return render(request, 'upload.html', context)


def view_images(request):
    images = Image.objects.all().order_by('-id')
    return render(request, 'images.html', {'images': images})


def view_image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'image.html', {'image': image})


@login_required
def my_images(request):
    my_images = Image.objects.filter(user=request.user).order_by('-id')
    return render(request, 'my_images.html', {'my_images': my_images})


