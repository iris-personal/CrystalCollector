from django.db import models
from django.urls import reverse
from datetime import date

CLEANSES = (
    ('S', 'Selenite'),
    ('W', 'Water'),
    ('I', 'Incense'),
    ('M', 'Moonlight')
)

class Cut(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cuts_detail', kwargs={'pk': self.id})


class Crystal(models.Model):
    name = models.CharField(max_length=50)
    colors = models.CharField(max_length=100)
    properties = models.TextField(max_length=250)
    cuts = models.ManyToManyField(Cut)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    def cleansed(self):
        today = date.today()
        return self.cleansing_set.filter(date__year=today.year, date__month=today.month).count() >= 1

class Photo(models.Model):
    url = models.CharField(max_length=200)
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for crystal_id: {self.crystal_id} @{self.url}"

class Cleansing(models.Model):
    date = models.DateField('Date of Last Cleanse')
    cleanse = models.CharField(
        'Method of Cleansing Used',
        max_length=1,
        choices=CLEANSES,
        default=CLEANSES[0][0]
        )

    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_cleanse_display()} on {self.date}"

    class Meta:
        ordering = ['-date']