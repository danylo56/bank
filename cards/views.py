from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from cards.forms import CardCreationForm
from cards.models import Card
from cards.utils import create_bill_number


class UserCardListView(LoginRequiredMixin, generic.ListView):
    model = Card
    template_name = 'cards/cards.html'
    context_object_name = 'user_cards'

    def get_queryset(self):
        return self.model.objects.filter(holder=self.request.user)


class CreateCardView(LoginRequiredMixin, generic.CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': CardCreationForm()}
        return render(request, 'cards/create.html', context)

    def post(self, request, *args, **kwargs):
        form = CardCreationForm(request.POST)
        if form.is_valid():
            card_type = form.cleaned_data['type']
            bill_number = create_bill_number(card_type == '1')
            while len(Card.objects.filter(bill_number=bill_number)) > 0:
                bill_number = create_bill_number(card_type == '1')
            holder = request.user
            card = Card.objects.create(holder=holder, bill_number=bill_number, balance=0)
            card.save()
            return HttpResponseRedirect(reverse_lazy('my_cards'))
        return render(request, 'cards/create.html', {'form': form})


