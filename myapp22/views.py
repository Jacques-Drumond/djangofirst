from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.POST['text']
    res = len(words.split())
    context = {'number': res}
    return render(request, 'counter.html', context)

def gato(request):
    gatos = ['🐈', '🐱', '😿', '😽', '😹']
    faces = ['😀' , '😃' , '😄' , '😁', '😆', '😅', '😂', '🤣' ,'😊', '😇', '🙂', '🙃']
    objects = ['⛱️', '⏰', '🤿', '🎐' , '🕹️', '📯', '💎', '📱', '📻', '🔌', '💻', '🎥']
    context = {'gato': random.choice(gatos), 
    'face': random.choice(faces), 
    'obj':random.choice(objects)}
    return render(request, 'gatio.html', context)