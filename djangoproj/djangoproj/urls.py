"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from gorodapi import views


app_name = 'gorodapi'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/<int:book_id>', views.book, name='book'),
    path('api/collection/<int:col_id>', views.collection_by_id, name='collectionId'),
    path('api/collection/<str:col_name>', views.collection_by_name, name='collectionName'),
]
