from django.db import models

# Create your models here.
class Profile(models.Model):  
    #other fields here
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image= models.URLField(blank=True)


    def __str__(self):  
        return f"{self.first_name}-{self.last_name}-{self.email}-{self.image}"


          