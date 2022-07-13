from django.forms import ModelForm
from .models import Stat

class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']