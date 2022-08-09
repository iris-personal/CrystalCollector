from pickle import FALSE
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.forms import CleansingForm
from .models import Crystal

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def crystals_index(request):
  crystals = Crystal.objects.all()
  return render(request, 'crystals/index.html', { 'crystals': crystals })
def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  cleansing_form=CleansingForm()
  return render(request, 'crystals/detail.html', {
    'crystal': crystal, 'cleansing_form': cleansing_form
    })

class CrystalCreate(CreateView):
  model = Crystal
  fields = '__all__'
  success_url = '/crystals/'

class CrystalUpdate(UpdateView):
  model = Crystal
  fields = ['colors', 'properties']

class CrystalDelete(DeleteView):
  model = Crystal
  success_url = '/crystals/'

def add_cleansing(request, crystal_id):
  form = CleansingForm(request.POST)
  if form.is_valid():
    new_cleansing = form.save(commit=False)
    new_cleansing.crystal_id = crystal_id
    new_cleansing.save()
  return redirect('detail', crystal_id=crystal_id)