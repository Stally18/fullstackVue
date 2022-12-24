from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import *
# Create your views here.


def book(request, book_id):
    book = Books.objects.get(id=book_id)
    return JsonResponse(model_to_dict(book))


def collection_by_id(request, col_id):
    collection = Collections.objects.get(id=col_id)
    books = []
    for book in collection.Books.iterator():
        books.append(model_to_dict(book))
    #books = []
    #for book in collection.Books.iterator():
    #    books.append(book)
    #books = collection.Books.iterator()
    #for book in collection.Books.iterator():
    #    books.append(model_to_dict(book))
    return JsonResponse(books, safe=False)

def collection_by_name(request, col_name):
    collection = Collections.objects.get(Name=col_name)
    books = []
    for book in collection.Books.iterator():
        books.append(model_to_dict(book))
    return JsonResponse(books, safe=False)
