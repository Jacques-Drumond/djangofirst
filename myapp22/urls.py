from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('gato', views.emoji, name='counter'),
    path('teste', views.teste, name='teste'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]