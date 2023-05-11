from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('afisha', views.afisha, name='afisha'),
    path('book', views.book, name='book'),
    path('shema', views.shema, name='shema'),
]
