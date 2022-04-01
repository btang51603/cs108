from django.shortcuts import render

# Create your views here.
from .models import Profile
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from .forms import CreateProfileForm, UpdateProfileForm
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''
    model= Profile
    template_name= "mini_fb/show_all_profiles.html"
    context_object_name = 'All_Profiles'

class ShowProfilePageView(DetailView):
    model= Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "Profile"

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm # which form to use to create the Profile
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Profile # which model to create
    form_class = UpdateProfileForm # which form to use to create the Quote
    template_name = "mini_fb/update_profile_form.html" # delegate the display to this template