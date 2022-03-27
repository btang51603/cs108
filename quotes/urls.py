#quotes/urls.py

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView

urlpatterns = [
    # map the URL (empty string) to the view
    path('', HomePageView.as_view(), name='home'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
    path('', RandomQuotePageView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view(), name="person"), ## NEW URL TO SHOW PERSON PAGE
]