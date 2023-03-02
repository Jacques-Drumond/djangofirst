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
        self.poke_name = str(poke_name).lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.poke_name}")
        if response.status_code == 200:
            self.data = response.json()
            self.poke_img = self.data['sprites']['front_default']
            self.poke_img2 = self.data['sprites']['back_default']
            self.poke_name = str(poke_name).capitalize()
            self.poketype = str(self.data['types'][0]['type']['name']).capitalize()
            poketypes = ['Fire', 'Water', 'Electric', 'Rock', 'Grass', 'Steel']
            poke_color = ['Red', 'Blue', 'Yellow', 'Grey', 'Green', 'Grey']
            self.poke_dict = dict(zip(poketypes, poke_color))
            try:
                self.poke_color = self.poke_dict.get(self.poketype).lower()
            except:
                self.poke_color = 'Black'
        else:
            self.poke_img = None

