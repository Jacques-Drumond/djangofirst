from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Emoji
import random

def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.POST['text']
    res = len(words.split())
    context = {'number': res}
    return render(request, 'counter.html', context)

def emoji(request):
    emojis = Emoji()
    emojis.is_emoji = False
    context = {'emoji':emojis}
    return render(request, 'gatio.html', context)


def teste(request):
    return render(request, 'teste.html')