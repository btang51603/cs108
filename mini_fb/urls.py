from django.urls import path
from .views import ShowAllProfilesView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='ShowAllProfiles'), # generic class-based view
]