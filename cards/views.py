from django.views import generic
from cards.models import Card


class UserCardListView(generic.ListView):
    model = Card
    template_name = 'cards/cards.html'
    context_object_name = 'user_cards'

    def get_queryset(self):
        return self.model.objects.filter(holder=self.request.user)
