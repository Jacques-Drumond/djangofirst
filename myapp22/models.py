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
        poke_name = str(poke_name).lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}")
        if response.status_code == 200:
            data = response.json()
            self.poke_img = data['sprites']['front_default']
            self.poke_name = str(poke_name).capitalize()
            self.poketype = str(data['types'][0]['type']['name']).capitalize()
            self.color = ''
            if self.poketype == 'Fire':
                self.color = 'Red'
            elif self.poketype == 'Water':
                self.color = 'Blue'
            elif self.poketype == 'Electric':
                self.color = 'Yellow'
            elif self.poketype == 'Rock':
                self.color = 'Grey'
            elif self.poketype == 'Grass':
                self.color = 'Green'
            else:
                self.color = 'Black'
        else:
            self.poke_img = None

