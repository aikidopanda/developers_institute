"""
URL configuration for giphy_project project.

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
from django.urls import path
from gifs.views import homepage_view, add_gif, add_category, gif_view, categories_view, category_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage_view),
    path('addgif/',add_gif),
    path('addcategory/',add_category),
    path('gifview/<int:id>',gif_view),
    path('categoriesview/', categories_view),
    path('categoryview/<int:cat_id>', category_view)
]
