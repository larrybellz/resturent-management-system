from django.db import models
from django.utils import timezone
from django.urls import reverse





class StockItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    description=models.TextField()
    date_updated=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})

