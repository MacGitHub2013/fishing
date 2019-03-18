from django.db import models
from django.urls import reverse
# Create your models here.

class Fish(models.Model):
    CHOICES = (
        ('fr','Fresh Water'),
        ('br','Brekish Water'),
        ('bo','Both')
    )
    name = models.CharField(max_length=120)
    alias=models.CharField(max_length = 500, null=True,blank=True)
    fish_type = models.CharField(max_length =2, choices=CHOICES )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('fish', args=[self.pk])