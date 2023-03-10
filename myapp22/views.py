from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
from .models import Emoji, Pokemon
import os

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':   
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')   
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def counter(request):
    words = request.POST['text']
    res = len(words.split())
    context = {'number': res}
    return render(request, 'counter.html', context)

def emoji(request):
    emojis = Emoji()
    emojis.is_emoji = True
    context = {'emoji':emojis}
    return render(request, 'gatio.html', context)

def teste(request):
    posts = [1,2,3,4, 'jacques', 'brabo'] 
    return render(request, 'teste.html', {'posts':posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def gato(request):
    dir_path = "static\media"

    file_list = os.listdir(dir_path)

    images = [i for i in file_list]

    images = ['static/media/' + filename for filename in images]

    return render(request, 'gatio.html', {'testes': images})

def pokeform(request):
    return render(request, 'pokeform.html')

def pokeresult(request):
    text = request.POST.get('text')
    if request.method == 'POST' and text != '':
        pokemon = Pokemon(poke_name=text)
        return render(request, 'pokeresult.html', {'pokemon': pokemon})
    else:
        return render(request, 'pokeresult.html')