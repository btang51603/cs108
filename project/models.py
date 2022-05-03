from django.db import models
from django.urls import reverse
# Create your models here.

class Deck(models.Model):
    contents = models.TextField(blank=True)
    author = models.TextField(blank=True)
    gameplan = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    title = models.TextField(blank=True)
    image= models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of the status message'''

        return self.author + self.contents + self.gameplan + str(self.price) + self.title
    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("show_deck", kwargs={"pk": self.pk})

class Profile(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):  
        return f"{self.first_name}-{self.last_name}-{self.email}-{self.address}"
    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("home")

class Rental(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    date_rented = models.DateTimeField(blank = True)
    date_return = models.DateTimeField(blank = True)
    
    def __str__(self):  
        return f"{self.date_rented}-{self.date_return}-{self.profile}-{self.deck}"
    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("show_all_rentals")




    