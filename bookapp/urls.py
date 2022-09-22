from django.urls import path

from .views import *

urlpatterns = [
    path('authors', AuthorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('authors/<str:pk>', AuthorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
    })),

    path('books', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('books/<str:pk>', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
    })),
]
