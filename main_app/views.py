from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Crystal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, type, colors, properties):
    self.type = type
    self.colors = colors
    self.properties = properties

crystals = [
  Crystal('Moss Agate', 'green and white', 'new beginnings and opening the heart'),
  Crystal('Green Strawberry Quartz', 'green', 'love, joy, recognition and allowing yourself to receive praise'),
  Crystal('Sodalite', 'blue and white', 'truth, focus, clarity and being authentic to self')
]

def home(request):
  return HttpResponse('<h1>Hello, Crystal Lovers</h1>')
def about(request):
  return render(request, 'about.html')
def crystals_index(request):
  return render(request, 'crystals/index.html', { 'crystals': crystals })