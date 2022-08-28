from django import forms
from django.forms import ModelForm
from .models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        if Subscription.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email
