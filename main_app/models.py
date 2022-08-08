from django.db import models
from django.urls import reverse

class Crystal(models.Model):
    type = models.CharField(max_length=50)
    colors = models.CharField(max_length=100)
    properties = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
