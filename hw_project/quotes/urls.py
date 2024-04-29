from django.urls import path,include

from . import views
from quotes.views import author_quotes, list_author, tag, tag_detail

app_name = "quotes"


urlpatterns = [
    path("", views.main, name='main'),
    path("<int:page>", views.main, name='root_paginate'),
    path("add_author", views.add_author, name="add_author"),
    path("add_quote", views.add_quote, name="add_quote"),
    path('tag/', views.tag, name='tag'),
    path('author/<str:author_name>/',list_author, name='author'),
    path('tag/<str:tag_name>/', tag_detail, name='tag_detail'),
    
]
