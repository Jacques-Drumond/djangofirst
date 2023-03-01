from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('teste', views.teste, name='teste'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path(f'post/<str:pk>', views.post, name='post'),
    path('gato', views.gato, name='post'),
    path('pokeform', views.pokeform, name='post'),
    path('pokeresult', views.pokeresult, name='post')
]