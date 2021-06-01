from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import EmailSubscriptionForm
from .utils import send_verification_email


class EmailSubscriptionFormView(FormView):
    template_name = "newsletter/thanks.html"
    form_class = EmailSubscriptionForm
    success_url = "/newsletter/ok"

    def form_valid(self, form):
        send_verification_email(form.cleaned_data["email"])
        # Even if we already have the email, we return the same response,
        # so noone knows if the email is alrready in use.
        return super().form_valid(form)


class NewsletterOkView(TemplateView):
    template_name = "newsletter/thanks.html"
