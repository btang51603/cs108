from django.contrib import admin
from .models import Profile, Deck, Rental
# Register your models here.
admin.site.register(Deck)
admin.site.register(Profile)
admin.site.register(Rental)