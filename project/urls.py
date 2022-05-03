from django.urls import path
from .views import ShowAllDecks, ShowDecks, CreateProfileView, CreateRentalView, ShowAllRentals, DeleteRentalView
urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllDecks.as_view(), name='home'), # generic class-based view
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), 
    path('deck/<int:pk>', ShowDecks.as_view(), name='show_deck'),
    path('create_rental', CreateRentalView.as_view(), name='create_rental'), 
    path('show_all_rentals', ShowAllRentals.as_view(), name='show_all_rentals'),
    path('show_all_rentals/delete_rental/<int:rental_pk>', DeleteRentalView.as_view(), name='delete_rental'),
]