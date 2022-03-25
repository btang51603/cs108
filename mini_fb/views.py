from django.shortcuts import render

# Create your views here.
from .models import mini_fb
from django.views.generic import ListView
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''
    model= mini_fb
    template_name= "mini_fb/show_all_profiles.html"
    context_object_name = 'mini_fb'
