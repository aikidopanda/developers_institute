"""
URL configuration for FilmProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from films.views import homepage, addFilm, addDirector, FilmDeleteView, DirectorDeleteView, sfd, sdd, CommentCreateView, RatingCreateView
from accounts.views import SignUpView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView
# from .settings import AUTH_USER_MODEL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage, name='homepage'),
    path('addfilm/', addFilm.as_view(), name = 'addFilm'),
    path('adddirector/', addDirector),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('accounts/login', LoginView.as_view(), name = 'login'),
    path('accounts/logout', LogoutView.as_view(), name = 'logout'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('deletefilm/<int:pk>', FilmDeleteView.as_view(), name='deletefilm'),
    path('films/sfd/', sfd, name='sfd'),
    path('director/sfd/', sdd, name='sdd'),
    path('deletedirector/<int:pk>', DirectorDeleteView.as_view(), name='deletedirector'),
    path('homepage/comment/<int:pk>', CommentCreateView.as_view(template_name = 'homepage.html'), name='comment'),
    path('homepage/rating/<int:pk>', RatingCreateView.as_view(template_name = 'homepage.html'), name='rating'),
]
