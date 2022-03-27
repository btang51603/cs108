#quotes/urls.py

from django.urls import path
from .views import HomePageView, QuotePageView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', HomePageView.as_view(), name='home'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
]