from django import forms
from .models import Reservation
import re

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['passenger_name', 'passport_number', 'seat_class', 'extra_luggage']
        widgets = {
            'passenger_name': forms.TextInput(attrs={'id': 'fullName', 'placeholder': 'John Doe'}),
            'passport_number': forms.TextInput(attrs={'id': 'passport', 'placeholder': 'A1234567'}),
            'seat_class': forms.Select(attrs={'id': 'seatClass'}),
            'extra_luggage': forms.CheckboxInput(attrs={'id': 'luggage'}),
        }

    def clean_passport_number(self):
        passport = self.cleaned_data.get('passport_number')
        # Regex validation on server side
        if not re.match(r'^[A-Z0-9]{6,9}$', passport):
            raise forms.ValidationError("Invalid passport format (6-9 alphanumeric characters).")
        return passport