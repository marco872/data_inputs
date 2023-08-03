

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, LoftRentals  # Import the LoftRentals class

class LoftRentalsForm(forms.ModelForm):
    class Meta:
        model = LoftRentals
        fields = ['rent_value_euro', 'present_status', 'rental_period_from', 'rental_period_to', 'loft_number']
        labels = {
            'rent_value_euro': 'Rent Value (Euro)',
            'present_status': 'Present Status',
            'rental_period_from': 'Rental Period From',
            'rental_period_to': 'Rental Period To',
            'loft_number': 'Loft Number',
        }

class CustomUserCreationForm(UserCreationForm):
    # Add any additional fields or customization here
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    useremail = forms.EmailField(max_length=254, required=True)
    # You can add more fields as needed
    # Remove default help_text for the username field
    username = forms.CharField(
        max_length=150,
        help_text='',  # Empty string to remove the default help text
        validators=[UnicodeUsernameValidator()],
    )

    password1 = forms.CharField(
        max_length=150,
        help_text='',  # Empty string to remove the default help text
        validators=[UnicodeUsernameValidator()],
    )


    password2 = forms.CharField(
        max_length=150,
        help_text='',  # Empty string to remove the default help text
        validators=[UnicodeUsernameValidator()],
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'firstname', 'lastname', 'useremail', 'password1', 'password2']
