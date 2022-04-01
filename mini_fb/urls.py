from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView,CreateProfileView, UpdateProfileView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='ShowAllProfiles'), # generic class-based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='ShowProfilePage'), # generic class-based view
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), 
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile")
]