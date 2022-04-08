from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView,CreateProfileView, UpdateProfileView,post_status_message, DeleteStatusMessageView, ShowNewsFeedView  # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='ShowAllProfiles'), # generic class-based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # generic class-based view
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), 
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/post_status', post_status_message, name="post_status"),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"), # NEW
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name = "news_feed")
]