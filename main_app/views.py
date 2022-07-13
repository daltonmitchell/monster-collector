from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster
from .forms import StatForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/index.html', { 'monsters': monsters })

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    stat_form = StatForm()
    return render(request, 'monsters/detail.html', { 'monster': monster, 'stat_form': stat_form })

class MonsterCreate(CreateView):
    model = Monster
    fields = '__all__'

class MonsterUpdate(UpdateView):
    model = Monster
    fields = ['name', 'type', 'size']

class MonsterDelete(DeleteView):
    model = Monster
    success_url = '/monsters/'

def add_stat(request, monster_id):
    form = StatForm(request.POST)
    if form.is_valid():
        new_stat = form.save(commit=False)
        new_stat.monster_id = monster_id
        new_stat.save()
    return redirect('detail', monster_id=monster_id)