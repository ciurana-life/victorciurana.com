from app.newsletter.forms import EmailSubscriptionForm
from django.urls import path

from .views import EmailSubscriptionFormView, NewsletterOkView

urlpatterns = [
    path(
        "subscribe/",
        EmailSubscriptionFormView.as_view(),
        name="subscribe",
    ),
    path("ok/", NewsletterOkView.as_view(), name="ok"),
]
