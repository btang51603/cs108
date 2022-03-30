from django.shortcuts import render

# Create your views here.
from .models import Profile
from django.views.generic import ListView,DetailView
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''
    model= Profile
    template_name= "mini_fb/show_all_profiles.html"
    context_object_name = 'All_Profiles'

class ShowProfilePageView(DetailView):
    model= Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "Profile"


