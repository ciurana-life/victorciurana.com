from django.forms import ModelForm

from .models import EmailSubscription


class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ["email"]
