from django.db import models
from django.urls import reverse

CLEANSES = (
    ('S', 'Selenite'),
    ('W', 'Water'),
    ('I', 'Incense'),
    ('M', 'Moonlight')
)

class Crystal(models.Model):
    type = models.CharField(max_length=50)
    colors = models.CharField(max_length=100)
    properties = models.TextField(max_length=250)

    def __str__(self):
        return self.type
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})

class Cleansing(models.Model):
    date = models.DateField()
    cleanse = models.CharField(
        max_length=1,
        choices=CLEANSES,
        default=CLEANSES[0][0]
        )

    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_cleanse_display()} on {self.date}"