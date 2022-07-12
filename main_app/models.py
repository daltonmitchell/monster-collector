from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})