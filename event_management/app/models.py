from django.db import models

# Create your models here.
class Venue(models.Model):
    name=models.CharField(max_length=200,blank=False)
    adress=models.CharField(max_length=200,blank=False)
    capacity=models.IntegerField(blank=False)

    def __str__(self):
        return self.name

class Event(models.Model):
    title=models.CharField(max_length=200,blank=False)
    description=models.CharField(max_length=200,blank=False)
    event_data=models.DateField(blank=False)
    venue=models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer=models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.title

