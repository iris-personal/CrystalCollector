from django.db import models

class Crystal(models.Model):
    type = models.CharField(max_length=50)
    colors = models.CharField(max_length=100)
    properties = models.TextField(max_length=250)
