from django.db import models
from aps_api.utils.validationFields import numbers_validator, letters_validator


class Names(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)  # 2 miembro
    second_name = models.CharField(max_length=60, null=True, blank=True, validators=[letters_validator])  # 3 miembro
    last_name = models.CharField(max_length=60, validators=[letters_validator])  # 4 miembro
    second_last_name = models.CharField(max_length=60, null=True, blank=True, validators=[letters_validator])  # 5 miembro
    id_document = models.CharField(max_length=20, validators=[numbers_validator], db_index=True)
    # 7 de miembro de familia  20 de responsable 17 de representante
# OK
