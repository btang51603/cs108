from django.shortcuts import render
from .models import Profile, Deck, Rental
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from .forms import CreateProfileForm, CreateRentalForm
from django.views.generic.edit import DeleteView
from django.urls import reverse
# Create your views here.

class ShowAllDecks(ListView):
    model = Deck # retrieve objects of type Quote from the database
    template_name = 'project/home.html'
    context_object_name = 'decks' # how to find the data in the template file

class ShowAllRentals(ListView):
    model = Rental # retrieve objects of type Quote from the database
    template_name = 'project/show_all_rentals.html'
    context_object_name = 'rentals' # how to find the data in the template file

class ShowDecks(DetailView):
    model = Deck
    template_name = 'project/show_deck.html'
    context_object_name = 'decks'

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm # which form to use to create the Profile
    template_name = "project/create_profile_form.html"

class CreateRentalView(CreateView):
    model = Rental
    form_class = CreateRentalForm
    template_name = "project/create_rental_form.html"

class DeleteRentalView(DeleteView):
    '''A view to delete a quote and remove it from the database.'''
    template_name = "project/delete_rental_form.html"
    queryset = Rental.objects.all()

    def get_success_url(self):
        
        rent = Rental.objects.get(pk=self.kwargs['rental_pk'])
        return reverse('show_all_rentals')
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(DeleteRentalView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        rent = Rental.objects.get(pk=self.kwargs['rental_pk'])
        context['rental'] = rent
        # return this context dictionary
        return context
    
    def get_object(self):
        rental_pk = self.kwargs['rental_pk']
        rent = Rental.objects.get(pk=self.kwargs['rental_pk'])

        return rent