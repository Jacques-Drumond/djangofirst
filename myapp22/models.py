from django.db import models
import random
# Create your models here.

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
