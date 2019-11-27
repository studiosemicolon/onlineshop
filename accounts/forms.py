from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from .models import Profile

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))


class SignUpForm(UserCreationForm):

    phone_number = forms.CharField(max_length=17)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone_number = forms.CharField(
        required=True, max_length=30, label=("phone"))
    full_name = forms.CharField(required=True)
    # = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())

    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=("Password(again)"))
    email = forms.EmailField(label=("E-mail"), widget=forms.EmailInput,)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'email', 'birth_date', 'phone_number', 'gender', 'password1', 'password2',)
