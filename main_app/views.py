from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  return render(request, 'crystals/detail.html', { 'crystal': crystal })

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