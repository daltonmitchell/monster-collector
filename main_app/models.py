from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class Env(models.Model):
    environment = models.CharField(max_length=50)

    def __str__(self):
        return self.environment

    def get_absolute_url(self):
        return reverse('env_detail', kwargs={'pk': self.id})

class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    envs = models.ManyToManyField(Env)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})

class Stat(models.Model):
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self}"