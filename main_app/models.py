from unicodedata import name
from django.db import models

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)