from django.shortcuts import render

# Create your views here.
from .models import Quote, Person
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import random
from .forms import CreateQuoteForm, UpdateQuoteForm 

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Quote # retrieve objects of type Quote from the database
    template_name = 'quotes/home.html'
    context_object_name = 'quotes' # how to find the data in the template file

class QuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'
    
class RandomQuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    ## note: reusing same template as DetailView to show one quote!!
    context_object_name = 'quote'

    # pick one quote at random:
    def get_object(self):
        '''Return one Quote object chosen at random.'''
		
        all_quotes = Quote.objects.all()
        return random.choice(all_quotes)
class PersonPageView(DetailView):
    '''Show all quotes and all images for one person.'''

    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'

class CreateQuoteView(CreateView):
    '''Create a new Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = CreateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the dispay to this template

class UpdateQuoteView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = UpdateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the display to this template
    