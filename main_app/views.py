import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.forms import CleansingForm
from .models import Crystal, Cut, Photo

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
  id_list = crystal.cuts.all().values_list('id')
  cuts_crystal_doesnt_have = Cut.objects.exclude(id__in=id_list)
  cleansing_form=CleansingForm()
  return render(request, 'crystals/detail.html', {
    'crystal': crystal, 
    'cleansing_form': cleansing_form,
    'cuts': cuts_crystal_doesnt_have
    }
  )

def assoc_cut(request, crystal_id, cut_id):
  Crystal.objects.get(id=crystal_id).cuts.add(cut_id)
  return redirect('detail', crystal_id=crystal_id)

def unassoc_cut(request, crystal_id, cut_id):
  Crystal.objects.get(id=crystal_id).cuts.remove(cut_id)
  return redirect('detail', crystal_id=crystal_id)

def add_photo(request, crystal_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, crystal_id=crystal_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(CreateView):
  model = Crystal
  fields = ['name', 'colors', 'properties']
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

class CutList(ListView):
  model = Cut

class CutDetail(DetailView):
  model = Cut

class CutCreate(CreateView):
  model = Cut
  fields = '__all__'

class CutUpdate(UpdateView):
  model = Cut
  fields = ['name']

class CutDelete(DeleteView):
  model = Cut
  success_url = '/cuts/'