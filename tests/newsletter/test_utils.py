import pytest

from app.newsletter.utils import send_verification_email



@pytest.mark.django_db
def test_cant_verify_existing_email(email_subscription):


# Can verify

# MODEL
# On save creates urltoken
# model.send_email calls celery task

# view for that url verification

# Then develop the on save for BlogPost to send mails

# And the unsibscribing!