from django.forms import ModelForm
from .models import Cleansing

class CleansingForm(ModelForm):
  class Meta:
    model = Cleansing
    fields = ['date', 'cleanse']