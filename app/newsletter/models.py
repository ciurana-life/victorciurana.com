from django.db import models
from django.core.validators import validate_email


class EmailSubscription(models.Model):
    email = models.EmailField(max_length=254, unique=True, validators=[validate_email])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    validated = models.BooleanField(
        default=False, help_text="Was the email validated by the user?"
    )

    def __str__(self):
        return f"Email {self.email}, validated {self.validated}"
