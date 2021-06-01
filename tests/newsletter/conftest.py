import pytest

from app.newsletter.models import EmailSubscription


@pytest.fixture()
def email_subscription():
    email_subscription = EmailSubscription.objects.create(
        email="admin@victorciurana.com"
    )
    return email_subscription
