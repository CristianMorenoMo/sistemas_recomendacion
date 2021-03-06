from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    """Default user for last-fm."""

    #: First and last name do not cover name patterns around the globe
