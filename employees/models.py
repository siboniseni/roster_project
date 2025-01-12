from django.db import models
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    working_hours = models.PositiveIntegerField()
    days_off = models.TextField()  # To store a JSON of days

    def __str__(self):
        return self.name
