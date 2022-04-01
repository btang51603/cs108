from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email = forms.CharField(label="Email", required=True)
    image = forms.URLField(label="image", required = True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email','image']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update an existing Quote object.'''
    email = forms.CharField(label="Email", required=True)
    image = forms.URLField(label="image", required = True)
    class Meta:
        '''additional data about this form'''
        model = Profile # which model to create
        fields = ['email','image'] # which fields to update

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to update an existing Quote object.'''
    class Meta:
        '''additional data about this form'''
        model = StatusMessage # which model to create
        fields = ['message'] # which fields to update