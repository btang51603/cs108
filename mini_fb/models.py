from django.db import models

# Create your models here.
class mini_fb(models.Model):  
    #other fields here
    First_name = models.TextField(blank=True)
    Last_name = models.TextField(blank=True)
    Email = models.EmailField(blank=True)
    Image= models.URLField(blank=True)


    def __str__(self):  
        return f"{self.First_name}-{self.Last_name}-{self.Email}-{self.Image}"
          