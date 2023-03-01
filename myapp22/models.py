from django.db import models
import random
# Create your models here.
import requests
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Emoji:
    def __init__(self):
        gatos = ['🐈', '🐱', '😿', '😽', '😹']
        faces = ['😀' , '😃' , '😄' , '😁', '😆', '😅', '😂', '🤣' ,'😊', '😇', '🙂', '🙃']
        objects = ['⛱️', '⏰', '🤿', '🎐' , '🕹️', '📯', '💎', '📱', '📻', '🔌', '💻', '🎥']
        self.is_emoji = bool
        self.gato = random.choice(gatos)
        self.face = random.choice(faces)
        self.objeto = random.choice(objects)


class Pokemon:
    def __init__(self, poke_name):
        self.poke_name = poke_name
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}")
        if response.status_code == 200:
            data = response.json()
            self.poke_img = data['sprites']['front_default']
        else:
            self.poke_img = None

