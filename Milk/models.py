from django.db import models
from django.utils import timezone
from Animals.models import Animal

class Status(models.TextChoices):
    morning="mn","morning"
    evening="ev","evening"

class Milk(models.Model):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)

    morning_qty = models.FloatField(default=0)
    evening_qty = models.FloatField(default=0)
    total_qty=models.FloatField(default=0) 

    def __str__(self):
        return str(self.animal)
    
    def save(self, *args, **kwargs):
        self.total_qty = self.morning_qty + self.evening_qty
        super().save(*args, **kwargs)
    

    class Meta:
        ordering=['-date']
        indexes=[models.Index(fields=['-date'])]