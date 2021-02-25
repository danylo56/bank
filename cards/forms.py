from django import forms


class CardCreationForm(forms.Form):
    CHOICES = [('1', 'VISA'), ('2', 'MasterCard')]
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
