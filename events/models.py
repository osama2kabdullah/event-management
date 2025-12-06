from django.db import models

# catagory
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# event
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')

    def __str__(self):
        return self.name

# participant
class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name='participants', blank=True)

    class Meta:
        unique_together = ['name', 'email']

    def __str__(self):
        return self.name
