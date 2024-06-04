from django.contrib.auth.models import User
from django.db import models
from .contact import Contact
from .names import Names
from aps_api.utils.validationFields import letters_validator
from ..properties import enums


class Pollster(models.Model):
    id = models.AutoField(primary_key=True)
    name_person = models.OneToOneField(Names, on_delete=models.CASCADE, db_index=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    job = models.IntegerField(choices=enums.OPTIONS_JOBS)  # 21
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
# OK
