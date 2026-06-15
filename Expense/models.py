from django.db import models
from django.utils import timezone

class Status(models.TextChoices):
    feed="fd","feed"
    medicine="md","medicine"
    mentainance="mn","mentainance"
    others="ot","others"

class Expense(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField()
    expense_type = models.CharField(max_length=2,choices=Status.choices,default=Status.feed)

    def __str__(self):
        return str(self.amount)
    
    class Meta:
        ordering=['-amount']
        indexes=[models.Index(fields=['-amount'])]
