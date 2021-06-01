import pytest

from app.newsletter.models import EmailSubscription


@pytest.mark.django_db
def test_email_subscription(email_subscription):
    es = EmailSubscription.objects.first()
    assert es.email == "admin@victorciurana.com"
    assert es.validated == False
