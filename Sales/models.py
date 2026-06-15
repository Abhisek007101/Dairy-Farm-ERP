from django.db import models
from django.utils import timezone

class Sale(models.Model):
    qty_sold=models.IntegerField()
    price=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    total_revenue = models.FloatField(default=0)
    

    def save(self, *args, **kwargs):
        self.total_revenue = self.qty_sold * self.price
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.qty_sold}L"
    
    class Meta:
        ordering=['-qty_sold']
        indexes=[models.Index(fields=['-qty_sold'])]