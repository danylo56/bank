from django.urls import path
from cards.views import UserCardListView, CreateCardView

urlpatterns = [
    path('', UserCardListView.as_view(), name="my_cards"),
    path('create', CreateCardView.as_view(), name="create_card"),
]