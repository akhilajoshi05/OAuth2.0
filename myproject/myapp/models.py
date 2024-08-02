# from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models
from oauth2_provider.models import AbstractApplication
from .validators import custom_validate_uris

class Application(AbstractApplication):
    allowed_origins = models.TextField(
        blank=True,
        validators=[custom_validate_uris],
        help_text="Allowed origins for CORS. Separate multiple origins with spaces.",
    )
# myapp/models.py

from django.db import models
from .validators import custom_validate_uris

class MyModel(models.Model):
    redirect_uris = models.JSONField(validators=[custom_validate_uris])
