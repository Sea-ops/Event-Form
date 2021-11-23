from django.db import models

# Create your models here.
class List(models.Model):
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)
    Event = models.CharField(max_length=100)
    Date = models.DateField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.Name} {self.Surname} {self.Event} {self.Date} {self.Address}'
