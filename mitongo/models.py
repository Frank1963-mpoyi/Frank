from django.db import models
from django.urls import reverse 





class RestaurantLocation(models.Model):
    title                       = models.CharField(max_length = 300)
    name                        = models.CharField(max_length = 100)
    description                 = models.TextField()
  

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('mitongo:Restaurant', kwargs ={'pk':self.pk})
