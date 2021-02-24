from django.urls import path
from cards.views import UserCardListView

urlpatterns = [
    path('', UserCardListView.as_view(), name="my_cards")
]