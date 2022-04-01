from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):  
    #other fields here
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image= models.URLField(blank=True)


    def __str__(self):  
        return f"{self.first_name}-{self.last_name}-{self.email}-{self.image}"
    
    def get_status_messages(self):
        '''Return all quotes for this Person.'''

        # use the object manager to filter Quotes by this person's pk:
        return StatusMessage.objects.filter(profile=self)
    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("ShowProfilePage", kwargs={"pk": self.pk})

class StatusMessage(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    def __str__(self):
        '''Return a string representation of the status message'''

        return str(self.time_stamp) + self.message 
    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("ShowProfilePage", kwargs={"pk": self.pk})



          