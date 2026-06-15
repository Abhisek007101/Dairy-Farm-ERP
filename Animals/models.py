from django.db import models
from django.utils import timezone



class Status(models.TextChoices):
    milking="mk","milking"
    dry="dy","dry"
    sold="sd","sold"


class Animal(models.Model):
    breed_name=models.CharField(max_length=100)
    tag_id=models.IntegerField(unique=True)
    animal_type=models.CharField(max_length=20)
    age=models.IntegerField()
    dob=models.DateTimeField(default=timezone.now)

    
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.sold)

    def __str__(self):
        return str(self.tag_id)
    
    class Meta:
        ordering=["-dob"]
        indexes=[models.Index(fields=["-dob"])]

        