from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from .models import Profile, StatusMessage
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.views.generic.edit import DeleteView
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''
    model= Profile
    template_name= "mini_fb/show_all_profiles.html"
    context_object_name = 'All_Profiles'

class ShowProfilePageView(DetailView):
    model= Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "Profile"
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm # which form to use to create the Profile
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Profile # which model to create
    form_class = UpdateProfileForm # which form to use to create the Quote
    template_name = "mini_fb/update_profile_form.html" # delegate the display to this template

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None) 

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

class DeleteStatusMessageView(DeleteView):
    '''A view to delete a quote and remove it from the database.'''
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_success_url(self):
        
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        profile_pk = self.kwargs['profile_pk']
        return reverse('show_profile_page', kwargs={'pk':profile_pk})
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['status_message'] = st_msg
        # return this context dictionary
        return context
    
    def get_object(self):
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        return st_msg

class ShowNewsFeedView(DetailView):
    model= Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "Profile"

        

        
    

