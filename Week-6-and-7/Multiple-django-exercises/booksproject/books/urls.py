from django.urls import path
from .views import BookList, BookDetail, book_create, BookUpdate

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/create-post/', book_create, name='book-create'),
    path('books/update/<int:pk>',BookUpdate.as_view(), name='book-update')
]