from django import forms
from django.contrib.auth.decorators import login_required

from .models import PropertyBook


class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))

    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest_numbers', 'children_numbers']
