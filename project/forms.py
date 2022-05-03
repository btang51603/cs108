from django import forms
from .models import Deck, Rental, Profile

class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email = forms.CharField(label="Email", required=True)
    address = forms.CharField(label="Address", required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email','address']

class CreateRentalForm(forms.ModelForm):
    '''A form to update an existing Quote object.'''
    date_rented = forms.DateTimeField(label="Date Rented", required=True)
    date_return = forms.DateTimeField(label="Date Returned", required=True)
   
    class Meta:
        '''additional data about this form'''
        model = Rental # which model to create
        fields = ['deck', 'date_rented', 'date_return', 'profile'] # which fields to update